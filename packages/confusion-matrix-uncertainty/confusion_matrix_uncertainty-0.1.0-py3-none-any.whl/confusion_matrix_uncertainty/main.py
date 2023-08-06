from pathlib import Path

import arviz
import numpy as np
import pandas as pd
import sympy
import typer

# CODE COPIED FROM https://github.com/niklastoe/classifier_metric_uncertainty

#%%

app = typer.Typer()

#%%


# sympy symbol definition for confusion matrix (CM) entries
symbol_order = "TP FN TN FP".split()
tp, fn, tn, fp = cm_elements = sympy.symbols(symbol_order)
n = sum(cm_elements)

distribution_samples = int(2e4)


class BetaBinomialDist(object):
    def __init__(self, k, j, prior=(0, 0)):
        self.k = k
        self.j = j
        self.n = k + j
        self.prior = prior
        self.theta_samples = self.sample_theta()
        self.theta_uncertainty = self.calc_uncertainty(self.theta_samples)
        self.pp_samples = self.posterior_predict_metric()
        self.pp_uncertainty = self.calc_uncertainty_list(self.pp_samples)

    def sample_theta(self):
        alpha = self.k + self.prior[0]
        beta = self.n - self.k + self.prior[1]
        return pd.Series(np.random.beta(alpha, beta, size=distribution_samples))

    def posterior_predict_metric(self):
        predicted_k = np.array(
            [np.random.binomial(self.n, x) for x in self.theta_samples.values]
        )
        predicted_j = self.n - predicted_k
        return pd.DataFrame({"k": predicted_k, "j": predicted_j})[["k", "j"]]

    @staticmethod
    def calc_hpd(dataseries, alpha=0.05):
        if isinstance(dataseries, (pd.DataFrame, pd.Series)):
            dataseries = dataseries.values
        return arviz.hdi(dataseries, alpha)

    def calc_uncertainty(self, distribution_samples):
        """calc 95% hpd length for a distribution which we consider a measure of uncertainty"""
        return np.diff(self.calc_hpd(distribution_samples))[0]

    def calc_uncertainty_list(self, table_of_distributions):
        """return uncertainty for all columns in a table (as defined by hpd interval length)"""
        metric_uncertainty = {}

        for i in table_of_distributions:
            metric_uncertainty[i] = self.calc_uncertainty(table_of_distributions[i])

        metric_uncertainty = pd.Series(metric_uncertainty)

        return metric_uncertainty


#%%


bayeslaplace_priors = {"TNR": [1, 1], "TPR": [1, 1], "PREVALENCE": [1, 1]}


def gelman_rubin(x):
    """Taken from PyMC3. Gelman and Rubin (1992)"""

    num_samples = x.shape[1]

    # Calculate between-chain variance
    B = num_samples * np.var(np.mean(x, axis=1), axis=0, ddof=1)

    # Calculate within-chain variance
    W = np.mean(np.var(x, axis=1, ddof=1), axis=0)

    # Estimate of marginal posterior variance
    Vhat = W * (num_samples - 1) / num_samples + B / num_samples

    return np.sqrt(Vhat / W)


class ConfusionMatrixAnalyser(BetaBinomialDist):
    def __init__(
        self,
        confusion_matrix,
        priors=bayeslaplace_priors,
        posterior_predictions=True,
    ):
        self.confusion_matrix = confusion_matrix
        self.priors = priors
        self.n = float(self.confusion_matrix.values.sum())
        self.metrics = get_metric_dictionary()
        self.cm_metrics = self.calc_metrics(self.confusion_matrix.astype(float))

        self.prevalence = BetaBinomialDist(
            self.confusion_matrix[["TP", "FN"]].sum(),
            self.confusion_matrix[["TN", "FP"]].sum(),
            prior=self.priors["PREVALENCE"],
        ).theta_samples

        self.tpr = BetaBinomialDist(
            self.confusion_matrix["TP"],
            self.confusion_matrix["FN"],
            prior=self.priors["TPR"],
        ).theta_samples

        self.tnr = BetaBinomialDist(
            self.confusion_matrix["TN"],
            self.confusion_matrix["FP"],
            prior=self.priors["TNR"],
        ).theta_samples

        self.theta_samples = self.sample_theta()
        self.theta_metrics = self.calc_metrics(self.theta_samples)
        self.theta_metric_uncertainty = self.calc_uncertainty_list(self.theta_metrics)

        # if we just want to look at the priors, we don't want posterior predictions because self.n=0
        if posterior_predictions:
            self.pp_samples = self.posterior_predict_confusion_matrices()
            self.pp_metrics = self.calc_metrics(self.pp_samples)
            self.pp_metric_uncertainty = self.calc_uncertainty_list(self.pp_metrics)

    def sample_theta(self):

        tp_samples = self.prevalence * self.tpr
        fn_samples = self.prevalence * (1 - self.tpr)
        tn_samples = (1 - self.prevalence) * self.tnr
        fp_samples = (1 - self.prevalence) * (1 - self.tnr)

        theta_samples = pd.DataFrame(
            {"TP": tp_samples, "FN": fn_samples, "TN": tn_samples, "FP": fp_samples}
        )

        if not self.gelman_rubin_test_on_samples(theta_samples.values):
            raise ValueError(
                "Model did not converge according to Gelman-Rubin diagnostics!!"
            )

        return theta_samples

    def posterior_predict_confusion_matrices(self, pp_n=None):

        if pp_n is None:
            pp_n = self.n

        posterior_prediction = np.array(
            [np.random.multinomial(pp_n, x) for x in self.theta_samples.values]
        )

        if not self.gelman_rubin_test_on_samples(posterior_prediction):
            raise ValueError(
                "Not enough posterior predictive samples according to Gelman-Rubin diagnostics!!"
            )

        return pd.DataFrame(posterior_prediction, columns=self.theta_samples.columns)

    @staticmethod
    def gelman_rubin_test_on_samples(samples):
        no_samples = len(samples)
        split_samples = np.stack(
            [samples[: int(no_samples / 2)], samples[int(no_samples / 2) :]]
        )
        passed_gelman_rubin = (gelman_rubin(split_samples) < 1.01).all()
        return passed_gelman_rubin

    def calc_metrics(self, samples):
        metrics_numpy_functions = self.metrics["numpy"]

        # pass samples to lambdified functions of metrics
        # important to keep the order of samples consistent with definition: TP, FN, TN, FP
        metrics_dict = {
            x: metrics_numpy_functions[x](*samples[symbol_order].values.T)
            for x in metrics_numpy_functions.index
        }

        # store in pandas for usability
        if type(samples) == pd.DataFrame:
            metrics = pd.DataFrame(metrics_dict)
        else:
            metrics = pd.Series(metrics_dict)

        return metrics


def get_metric_dictionary():
    metrics = {}

    metrics["PREVALENCE"] = (tp + fn) / n
    metrics["BIAS"] = (tp + fp) / n

    metrics["TPR"] = tpr = tp / (tp + fn)
    metrics["TNR"] = tnr = tn / (tn + fp)
    metrics["PPV"] = ppv = tp / (tp + fp)
    metrics["NPV"] = npv = tn / (tn + fn)
    metrics["FNR"] = 1 - tpr
    metrics["FPR"] = 1 - tnr
    metrics["FDR"] = 1 - ppv
    metrics["FOR"] = 1 - npv

    metrics["ACC"] = (tp + tn) / n

    mcc_upper = tp * tn - fp * fn
    mcc_lower = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)
    metrics["MCC"] = mcc_upper / sympy.sqrt(mcc_lower)

    metrics["F1"] = 2 * (ppv * tpr) / (ppv + tpr)
    metrics["BM"] = tpr + tnr - 1
    metrics["MK"] = ppv + npv - 1

    numpy_metrics = {
        x: sympy.lambdify(cm_elements, metrics[x], "numpy") for x in metrics
    }

    metrics_df = pd.DataFrame({"symbolic": metrics, "numpy": numpy_metrics})

    return metrics_df


#%%


def compare_classifiers(cm_analyser, cm_analyser2, metric="MCC"):
    is_better = cm_analyser.theta_metrics[metric] > cm_analyser2.theta_metrics[metric]
    return is_better.mean()


#%%


@app.command()
def main(filename: Path, metric: str = "MCC"):

    """
    Compare the different models using METRIC, optionally with a --metric.
    """

    df = pd.read_csv(filename, index_col=0)

    cm_ML = df.loc["ML__exclude_hospital", ["TP", "FN", "TN", "FP"]]
    cm_analyser_ML = ConfusionMatrixAnalyser(cm_ML)

    # cm_analyser_ML.theta_samples
    # cm_analyser_ML.theta_metrics

    for model in df.index:
        cm = df.loc[model, ["TP", "FN", "TN", "FP"]]
        analyser = ConfusionMatrixAnalyser(cm)
        P = compare_classifiers(analyser, cm_analyser_ML, metric=metric)
        typer.echo(f"{model+':':35s} \t {metric}, P = {P:.2%}")

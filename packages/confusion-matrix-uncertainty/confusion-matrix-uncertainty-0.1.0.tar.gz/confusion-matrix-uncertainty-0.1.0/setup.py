# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['confusion_matrix_uncertainty']

package_data = \
{'': ['*']}

install_requires = \
['arviz>=0.11.2,<0.12.0',
 'pandas>=1.2.4,<2.0.0',
 'sympy>=1.8,<2.0',
 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['confusion-matrix-uncertainty = '
                     'confusion_matrix_uncertainty.main:app']}

setup_kwargs = {
    'name': 'confusion-matrix-uncertainty',
    'version': '0.1.0',
    'description': '',
    'long_description': 'This is a test package',
    'author': 'Christian Michelsen',
    'author_email': 'christianmichelsen@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

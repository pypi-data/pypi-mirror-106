# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['onow']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.2.4,<1.3.0',
 'scikit-learn>=0.24.2,<0.25.0',
 'spacy>=3.0.6,<3.1.0',
 'torch>=1.8.1,<1.9.0',
 'torchtext>=0.9.1,<0.10.0']

setup_kwargs = {
    'name': 'onow',
    'version': '0.0.1',
    'description': 'Tools for chatbot data science.',
    'long_description': None,
    'author': 'Tangible AI',
    'author_email': 'engineering@tangibleai.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<4.0',
}


setup(**setup_kwargs)

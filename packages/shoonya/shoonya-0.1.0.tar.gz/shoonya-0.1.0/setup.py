# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['shoonya']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'shoonya',
    'version': '0.1.0',
    'description': 'Unofficial Trading APIs for Finvasia Shoonya Platform, help for algo traders',
    'long_description': None,
    'author': 'Algo 2 Trade',
    'author_email': 'help@algo2.trade',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

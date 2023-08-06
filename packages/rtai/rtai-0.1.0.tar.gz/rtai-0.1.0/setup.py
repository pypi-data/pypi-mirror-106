# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rtai']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rtai',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Simon Biggs',
    'author_email': 'me@simonbiggs.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ub_pypi']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ub-pypi',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ubani Balogun',
    'author_email': 'balogunubani@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

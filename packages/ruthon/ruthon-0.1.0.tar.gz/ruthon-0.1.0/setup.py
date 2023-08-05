# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ruthon']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'ruthon',
    'version': '0.1.0',
    'description': 'Russian-friendly python library',
    'long_description': None,
    'author': 'Dmitry Shchedrov',
    'author_email': 'shchedrov@pm.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

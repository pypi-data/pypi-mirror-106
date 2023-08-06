# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['secondstate']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'secondstate',
    'version': '1.0.2',
    'description': '',
    'long_description': None,
    'author': 'Lewis',
    'author_email': 'lewis@fruiti.app',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

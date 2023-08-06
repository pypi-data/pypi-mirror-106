# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jaswdr_rid']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'jaswdr-rid',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Jonathan Schweder',
    'author_email': 'jonathanschweder@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6.2,<4.0',
}


setup(**setup_kwargs)

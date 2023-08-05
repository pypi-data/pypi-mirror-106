# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snakypy']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'snakypy',
    'version': '0.4.0',
    'description': 'This is no longer a usable package. Now it\'s called "Snakypy Helpers."',
    'long_description': "========\nSnakypy\n========\n\n\nThis is no longer a usable package. Now it's called `Snakypy Helpers`_.\n\n.. _Snakypy Helpers: https://pypi.org/project/snakypy-helpers/\n",
    'author': 'William C. Canin',
    'author_email': 'william.costa.canin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

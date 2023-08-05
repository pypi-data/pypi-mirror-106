# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest_accept', 'pytest_accept.tests']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=6,<7']

entry_points = \
{'pytest11': ['accept = pytest_accept']}

setup_kwargs = {
    'name': 'pytest-accept',
    'version': '0',
    'description': 'A pytest-plugin for updating doctest outputs',
    'long_description': None,
    'author': 'max-sixty',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<3.10',
}


setup(**setup_kwargs)

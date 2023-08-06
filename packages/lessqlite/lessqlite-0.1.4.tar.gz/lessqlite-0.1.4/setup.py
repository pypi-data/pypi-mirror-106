# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lessqlite']

package_data = \
{'': ['*'], 'lessqlite': ['UNKNOWN.egg-info/*']}

install_requires = \
['click>=8.0.0,<9.0.0', 'coveralls>=3.0.1,<4.0.0']

entry_points = \
{'console_scripts': ['lessqlite = lessqlite.core:cli']}

setup_kwargs = {
    'name': 'lessqlite',
    'version': '0.1.4',
    'description': 'A less-like command-line tool for paging through SQLite databases.',
    'long_description': None,
    'author': 'Dave VanderWeele',
    'author_email': 'weele.me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dvanderweele/lessqlite',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dbml_sqlite']

package_data = \
{'': ['*'], 'dbml_sqlite': ['UNKNOWN.egg-info/*']}

install_requires = \
['click>=8.0.0,<9.0.0', 'pydbml>=0.3.4,<0.4.0']

entry_points = \
{'console_scripts': ['dbml_sqlite = dbml_sqlite.terminal:cli']}

setup_kwargs = {
    'name': 'dbml-sqlite',
    'version': '0.2.5',
    'description': 'A package that provides a CLI tool and a functional API for converting dbml files to SQLite DDL.',
    'long_description': None,
    'author': 'Dave VanderWeele',
    'author_email': 'weele.me@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dvanderweele/DBML_SQLite',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

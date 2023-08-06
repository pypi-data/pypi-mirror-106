# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['snakypy', 'snakypy.imake']

package_data = \
{'': ['*']}

install_requires = \
['snakypy-helpers>=0.1.4,<0.2.0', 'tomlkit>=0.7.2,<0.8.0']

entry_points = \
{'console_scripts': ['imake = snakypy.imake:main']}

setup_kwargs = {
    'name': 'imake',
    'version': '0.1.0a2',
    'description': '',
    'long_description': 'Imake is a command line tool to simplify commands in Python projects, discarding the usability of a Makefile file.',
    'author': 'William C. Canin',
    'author_email': 'william.costa.canin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/snakypy/imake',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lastfm_backup_cli']

package_data = \
{'': ['*']}

install_requires = \
['pylast>=4.2.1,<5.0.0']

entry_points = \
{'console_scripts': ['lastfm-backup = lastfm_backup_cli.main:cli_main']}

setup_kwargs = {
    'name': 'lastfm-backup-cli',
    'version': '0.1.0',
    'description': 'Super-simple CLI tool for backing up Last.fm scrobbling data',
    'long_description': None,
    'author': 'emkor93',
    'author_email': 'emkor93@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

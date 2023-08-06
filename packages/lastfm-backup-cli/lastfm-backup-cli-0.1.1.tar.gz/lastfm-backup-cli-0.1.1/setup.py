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
    'version': '0.1.1',
    'description': 'Super-simple CLI tool for backing up Last.fm scrobbling data',
    'long_description': '# lastfm-backup-cli\nSuper-simple CLI tool for backing up Last.fm scrobbling data into CSV file\n\n### installation\n- pre-requisites: Python 3.7 or newer, pip\n- `pip install --user lastfm-backup-cli`\n    - or `python3 -m pip install --user lastfm-backup-cli` if your default Python is 2.x\n\n### usage\n- get your LastFM API key [here](https://www.last.fm/api)\n- run `lastfm-backup <PATH TO BACKUP CSV FILE> --user <YOUR LASTFM USERNAME> --api-key <YOUR API KEY> --time-from <DATE OF FIRST SCROBBLE IN BACKUP FILE> --time-to <DATE OF LAST SCROBBLE IN BACKUP FILE>`\n    - example: `lastfm-backup lastfm-backup-2021-01.csv --user Rezult --api-key <YOUR API KEY> --time-from 2021-01-01 --time-to 2021-01-02`\n\n- output structure is:\n```csv\n<SCROBBLE DATE>,<SCROBBLE TIME (UTC)>,<ARTIST>,<TITLE>\n...\n```\n- output example:\n```csv\n2021-04-01,10:42:53,PRO8L3M,Backstage\n2021-04-01,10:39:59,PRO8L3M,Byłem tam\n2021-04-01,10:34:52,Deftones,Pompeji\n2021-04-01,10:30:14,Deftones,This Link Is Dead\n2021-04-01,10:26:38,Deftones,Radiant City\n2021-04-01,10:21:48,Deftones,Error\n2021-04-01,10:17:37,Deftones,Ohms\n2021-04-01,10:13:08,The Avalanches,Gold Sky\n2021-04-01,10:10:49,The Avalanches,Oh the Sunn!\n2021-04-01,10:07:18,The Avalanches,Overcome\n2021-04-01,10:03:56,The Avalanches,Music Makes Me High\n2021-04-01,09:59:34,The Avalanches,Reflecting Light\n2021-04-01,09:53:43,The Avalanches,Wherever You Go\n```\n',
    'author': 'emkor93',
    'author_email': 'emkor93@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/emkor/lastfm-backup-cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

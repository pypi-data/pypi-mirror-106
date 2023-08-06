# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyinaturalist_open_data', 'pyinaturalist_open_data.models']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4,<2.0',
 'boto3>=1.17,<2.0',
 'click-help-colors>=0.9,<0.10',
 'click>=7.1,<7.2',
 'pyinaturalist>=0.12.0,<0.13.0',
 'requests-cache>=0.6.3,<0.7.0',
 'rich>=10.0',
 'sqlalchemy>=1.4,<2.0']

entry_points = \
{'console_scripts': ['pynat = pyinaturalist_open_data.cli:pynat']}

setup_kwargs = {
    'name': 'pyinaturalist-open-data',
    'version': '0.1.1',
    'description': 'Python utilities for working with inaturalist-open-data',
    'long_description': "# pyinaturalist-open-data\n\n[![Build status](https://github.com/JWCook/pyinaturalist-open-data/workflows/Build/badge.svg)](https://github.com/JWCook/pyinaturalist-open-data/actions)\n[![PyPI](https://img.shields.io/pypi/v/pyinaturalist-open-data?color=blue)](https://pypi.org/project/pyinaturalist-open-data)\n[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/pyinaturalist-open-data)](https://pypi.org/project/pyinaturalist-open-data)\n[![PyPI - Format](https://img.shields.io/pypi/format/pyinaturalist-open-data?color=blue)](https://pypi.org/project/pyinaturalist-open-data)\n\n**This is a work in progress and not yet complete!**\n\n**pyinaturalist-open-data** is a python library and CLI tool for working with\n[inaturalist-open-data](https://github.com/inaturalist/inaturalist-open-data).\nIts goal is to make it easy to import and use this dataset in a python application backed by\n[any SQLAlchemy-compatible database engine](https://docs.sqlalchemy.org/en/14/core/engines.html#supported-databases)\n(SQLite by default), or simply for local data exploration.\n\nSee the CLI in action here or on [asciinema](https://asciinema.org/a/412516):\n[![asciicast](docs/pynat-demo.gif)](https://asciinema.org/a/412516)\n\n## Installation\nInstall with pip:\n```\npip install pyinaturalist-open-data\n```\n\nOr for local development:\n```bash\ngit clone https://github.com/JWCook/pyinaturalist-open-data.git\ncd pyinaturalist-open-data\npip install poetry && poetry install\n```\n\n## Usage\n\nThis package provides the command `pynat`. See `--help` for commands and options:\n```\nUsage: pynat [OPTIONS] COMMAND [ARGS]...\n\n  Commands for working with inaturalist open data\n\nOptions:\n  -v, --verbose  Show more detailed output\n  --help         Show this message and exit.\n\nCommands:\n  db    Load contents of CSV files into a database\n  dl    Download and extract inaturalist open data archive\n  init  Just create tables (if they don't already exist) without populating...\n  load  Download and load all data into a database.\n```\n\n### Run everything\nThe simplest command is `load`, which runs all steps:\n1. Download and extract the dataset\n2. Create database tables and indices\n3. Load the data into the database\n\nOptions:\n```\nUsage: pynat load [OPTIONS]\n\nOptions:\n  -d, --download-dir TEXT  Alternate path for downloads\n  -u, --uri TEXT           Alternate database URI to connect to\n  --help                   Show this message and exit.\n```\n\nBy default, this will create a new SQLite database. Alternatively, you can provide a URI for\n[any supported database](https://docs.sqlalchemy.org/en/14/core/engines.html#supported-databases).\n\n### Run individual steps\nOther commands are available if you only one to run one of those steps at a time.\n\n`dl` command:\n```\nUsage: pynat dl [OPTIONS]\n\n  Download and extract all files in the inaturalist open data archive\n\nOptions:\n  -d, --download-dir TEXT  Alternate path for downloads\n  --help                   Show this message and exit\n```\n\n**Note:** Both `dl` and `load` will reuse local data if already exists and is up to date.\n\n`db` command:\n```\nUsage: pynat db [OPTIONS]\n\n  Load contents of CSV files into a database. Also creates tables and\n  indexes, if they don't already exist.\n\nOptions:\n  -d, --download-dir TEXT         Alternate path for downloads\n  -i, --init                      Just initialize the database with tables\n                                  + indexes without loading data\n  -t, --tables [observation|photo|taxon|user]\n                                  Load only these specific tables\n  -u, --uri TEXT                  Alternate database URI to connect to\n\n  --help                          Show this message and exit.\n```\n\n**Note:** This can take a long time to run. Depending on the database type, you will likely get\nbetter performance with database-specific bulk loading tools (for example, `psql` with [COPY](https://www.postgresql.org/docs/13/sql-copy.html) for PostgreSQL)\n\n### Python package\nTo use as a python package instead of a CLI tool:\n```python\nfrom pyinaturalist_open_data import download_metadata, load_all\n\ndownload_metadata()\nload_all()\n```\n\nFull package documentation on readthedocs will be coming soon.\n\n## Planned features\nSome features I would ideally like to add to this:\n* Performance optimizations\n* Basic querying features\n* Image downloads based on query results\n* Integration with [iNaturalist API](https://api.inaturalist.org/v1/docs/#/) data via\n  [pyinaturalist](https://github.com/JWCook/pyinaturalist-open-data)\n* Integration with CSV data from the [iNaturalist export tool](https://www.inaturalist.org/observations/export)\n",
    'author': 'Jordan Cook',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/JWCook/pyinaturalist-open-data',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

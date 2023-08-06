# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['uroko']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0,<9.0.0', 'numpy>=1.20.3,<2.0.0']

entry_points = \
{'console_scripts': ['uroko-cli = uroko.cli:main']}

setup_kwargs = {
    'name': 'uroko',
    'version': '0.2.2',
    'description': 'Data scaling tool for CSV/TSV',
    'long_description': '# uroko\n\n[![PyPI version](https://badge.fury.io/py/uroko.svg)](https://pypi.org/project/uroko/)\n[![CircleCI](https://circleci.com/gh/t-chov/uroko.svg?style=svg)](https://app.circleci.com/pipelines/github/t-chov/uroko)\n[![Codecov](https://codecov.io/gh/t-chov/uroko/branch/main/graph/badge.svg)](https://app.codecov.io/gh/t-chov/uroko)\n\nData scaling tool for CSV/TSV\n\n"uroko" means scale in Japanese.\n\nInput CSV/TSV data, output min-max scaled data with some functions.\n\n## Usage\n\n```\nUsage: uroko-cli [OPTIONS] [INPUT] [OUTPUT]\n\nOptions:\n  --version               Show the version and exit.\n  -c, --columns TEXT      columns to scale\n  -a, --apply [log|sqrt]  apply whith calculation for scaling\n  --csv                   load as csv\n  --tsv                   load as tsv\n  --help                  Show this message and exit.\n```\n\n## Example\n\n### Plain\n\n```\n$ echo """name,score\nSato,100\nKimura,50\nSuzuki,80\n""" | uroko-cli -c score\nname,score\nSato,1.0\nKimura,0.0\nSuzuki,0.6\n```\n\n### Use log scale\n\n```\necho """name      value\nkyoto   10000\ngifu    100\ngumma   1\n""" | uroko-cli -c value -a log --tsv\nname    value\nkyoto   1.0\ngifu    0.4604718013624446\ngumma   0.0\n```\n',
    'author': 'Kohei Tsuyuki',
    'author_email': 'kotsuyuki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/t-chov/uroko',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)

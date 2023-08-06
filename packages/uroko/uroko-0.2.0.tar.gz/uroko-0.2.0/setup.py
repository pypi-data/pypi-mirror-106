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
    'version': '0.2.0',
    'description': 'Data scaling tool for CSV/TSV',
    'long_description': None,
    'author': 'Kohei Tsuyuki',
    'author_email': 'kotsuyuki@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)

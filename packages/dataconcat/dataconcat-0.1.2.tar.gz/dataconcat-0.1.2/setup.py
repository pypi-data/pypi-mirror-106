# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataconcat']

package_data = \
{'': ['*'], 'dataconcat': ['data/*']}

install_requires = \
['maya>=0.6.1,<0.7.0',
 'pandas>=1.2.4,<2.0.0',
 'pandera>=0.6.4,<0.7.0',
 'toolz>=0.11.1,<0.12.0',
 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['concat_mixer = dataconcat.mixer:app']}

setup_kwargs = {
    'name': 'dataconcat',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Kevin Hill',
    'author_email': 'kah.kevin.hill@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

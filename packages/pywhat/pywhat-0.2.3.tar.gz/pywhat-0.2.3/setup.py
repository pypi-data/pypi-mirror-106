# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pywhat']

package_data = \
{'': ['*'], 'pywhat': ['Data/*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'langdetect>=1.0.8,<2.0.0',
 'name_that_hash>=1.7.0,<2.0.0']

entry_points = \
{'console_scripts': ['pywhat = pywhat.what:main', 'what = pywhat.what:main']}

setup_kwargs = {
    'name': 'pywhat',
    'version': '0.2.3',
    'description': 'What is that thing?',
    'long_description': None,
    'author': 'Bee',
    'author_email': 'github@skerritt.blog',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clean_auckland_gtfs']

package_data = \
{'': ['*']}

install_requires = \
['gtfs_kit>=5']

setup_kwargs = {
    'name': 'clean-auckland-gtfs',
    'version': '0.5.0',
    'description': 'Python 3.8+ code for cleaning Auckland, New Zealand GTFS feeds',
    'long_description': None,
    'author': 'Alex Raichev',
    'author_email': 'araichev@mrcagney.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

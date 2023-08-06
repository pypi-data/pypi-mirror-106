# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiortc_pyav_stub']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiortc-pyav-stub',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Ulrich Petri',
    'author_email': 'ulo@ulo.pe',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

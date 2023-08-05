# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiopriman',
 'aiopriman.manager',
 'aiopriman.storage',
 'aiopriman.sync_primitives',
 'aiopriman.utils']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiopriman',
    'version': '0.2.0',
    'description': '',
    'long_description': None,
    'author': 'darksidecat',
    'author_email': 'bitalik371@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mason', 'mason.http', 'mason.nodes', 'mason.proto', 'mason.storages']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'protobuf>=3.13.0,<4.0.0', 'pyyaml>=5.3.1,<6.0.0']

extras_require = \
{'aiohttp': ['aiohttp>=3.7.4,<4.0.0', 'aiohttp_cors>=0.7.0,<0.8.0'],
 'sanic': ['sanic>=20.3.0,<21.0.0', 'sanic-cors>=0.10.0,<0.11.0']}

entry_points = \
{'console_scripts': ['mason = mason.cli:cli']}

setup_kwargs = {
    'name': 'mason-framework',
    'version': '0.0.11',
    'description': 'Node based building blocks.',
    'long_description': None,
    'author': 'Eric Hulser',
    'author_email': 'eric.hulser@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

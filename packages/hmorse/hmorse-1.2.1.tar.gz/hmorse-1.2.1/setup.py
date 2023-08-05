# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hmorse']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0,<9.0.0']

setup_kwargs = {
    'name': 'hmorse',
    'version': '1.2.1',
    'description': 'Morse code but h',
    'long_description': None,
    'author': 'vcokltfre',
    'author_email': 'vcokltfre@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

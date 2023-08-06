# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simplicial_test']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0',
 'matplotlib>=3.0.0,<4.0.0',
 'more-itertools>=8.7.0,<9.0.0',
 'numpy>=1.20.0,<2.0.0']

setup_kwargs = {
    'name': 'simplicial-test',
    'version': '1.2.0',
    'description': 'Simplicial-test implements an algorithm that realizes a simplicial complex from a prescribed joint degree sequence (if feasible).',
    'long_description': None,
    'author': 'Tzu-Chi Yen',
    'author_email': 'tzuchi.yen@colorado.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

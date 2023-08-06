# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastlid']

package_data = \
{'': ['*']}

install_requires = \
['fasttext>=0.9.2,<0.10.0', 'logzero>=1.7.0,<2.0.0']

setup_kwargs = {
    'name': 'fastlid',
    'version': '0.1.0',
    'description': 'Detect language via a fasttext model',
    'long_description': None,
    'author': 'freemt',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

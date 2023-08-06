# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fetch_embed']

package_data = \
{'': ['*']}

install_requires = \
['alive-progress>=1.6.2,<2.0.0',
 'httpx>=0.17.1,<0.18.0',
 'joblib>=1.0.1,<2.0.0',
 'loguru>=0.5.3,<0.6.0',
 'logzero>=1.7.0,<2.0.0',
 'numpy>=1.20.2,<2.0.0',
 'tqdm>=4.60.0,<5.0.0']

setup_kwargs = {
    'name': 'fetch-embed',
    'version': '0.1.4',
    'description': '',
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

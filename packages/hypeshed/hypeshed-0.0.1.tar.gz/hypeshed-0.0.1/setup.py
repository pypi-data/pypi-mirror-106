# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['hypeshed']

package_data = \
{'': ['*'], 'hypeshed': ['trakt/*']}

setup_kwargs = {
    'name': 'hypeshed',
    'version': '0.0.1',
    'description': 'A typestub package that defines types for public APIs',
    'long_description': None,
    'author': 'Bence Nagy',
    'author_email': 'bence@underyx.me',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

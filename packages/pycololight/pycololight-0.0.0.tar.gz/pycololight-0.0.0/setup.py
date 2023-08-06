# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pycololight']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pycololight',
    'version': '0.0.0',
    'description': 'Placeholds description',
    'long_description': '# pycololight\nA Python3 wrapper for interacting with LifeSmart ColoLight\n',
    'author': 'BazaJayGee66',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/BazaJayGee66/pycololight',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

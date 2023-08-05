# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['playing_cards']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'playing-cards',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'uyg',
    'author_email': 'ooy004003@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

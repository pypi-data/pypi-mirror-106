# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['factcast']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'factcast',
    'version': '0.0.1',
    'description': '',
    'long_description': None,
    'author': 'Eduard Thamm',
    'author_email': 'eduard.thamm@prisma-capacity.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

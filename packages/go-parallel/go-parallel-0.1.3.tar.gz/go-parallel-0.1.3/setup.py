# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['go_parallel']

package_data = \
{'': ['*']}

install_requires = \
['pydantic']

setup_kwargs = {
    'name': 'go-parallel',
    'version': '0.1.3',
    'description': 'Utility function for running functions asynchronously.',
    'long_description': None,
    'author': 'Indrajith Shetty',
    'author_email': 'indrajitshetty@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fitin']

package_data = \
{'': ['*']}

install_requires = \
['azure-appconfiguration>=1.1.1,<2.0.0',
 'azure-identity>=1.5.0,<2.0.0',
 'azure-keyvault-secrets>=4.2.0,<5.0.0',
 'environs>=9.3.1,<10.0.0']

setup_kwargs = {
    'name': 'fitin',
    'version': '0.3.0',
    'description': 'Simple config management, making it easy to write services that fit in.',
    'long_description': None,
    'author': 'peder2911',
    'author_email': 'pglandsverk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minos',
 'minos.api_gateway.common',
 'minos.api_gateway.common.client',
 'minos.api_gateway.common.configuration',
 'minos.api_gateway.common.rest']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'aiohttp>=3.7.4,<4.0.0',
 'aiomisc>=14.0.3,<15.0.0',
 'six>=1.16.0,<2.0.0']

setup_kwargs = {
    'name': 'minos-apigateway-common',
    'version': '0.0.3',
    'description': 'Python Package with common Classes and Utilities used in Minos API Gateway.',
    'long_description': 'API Gateway Common\n==================\n\nMinos Boilerplate contains all the boilerplate you need to create a Minos Python package.\n\n\nCredits\n-------\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)  and the [Minos Package](https://github.com/Clariteia/minos-pypackage) project template.\n',
    'author': 'Clariteia Devs',
    'author_email': 'devs@clariteia.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://clariteia.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minos',
 'minos.api_gateway.discovery',
 'minos.api_gateway.discovery.database',
 'minos.api_gateway.discovery.periodic']

package_data = \
{'': ['*']}

install_requires = \
['minos-apigateway-common>=0.0.3,<0.0.4', 'redis>=3.5.3,<4.0.0']

setup_kwargs = {
    'name': 'minos-discovery',
    'version': '0.0.1',
    'description': 'Minos Discovery service for Microservices subscription.',
    'long_description': 'Discovery Service\n=================\n\nMinos API Gateway Discovery Service\n\nCredits\n-------\n\nThis package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter)  and the [Minos Package](https://github.com/Clariteia/minos-pypackage) project template.\n',
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

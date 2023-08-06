# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minos',
 'minos.saga',
 'minos.saga.definitions',
 'minos.saga.executions',
 'minos.saga.executions.executors']

package_data = \
{'': ['*']}

install_requires = \
['dependency-injector>=4.32.2,<5.0.0', 'minos-microservice-common>=0.0,<0.1']

setup_kwargs = {
    'name': 'minos-microservice-saga',
    'version': '0.0.3',
    'description': 'Saga Library for MinOS project.',
    'long_description': 'Minos Microservice Saga\n=======================\n\n[![codecov](https://codecov.io/gh/Clariteia/minos_microservice_saga/branch/main/graph/badge.svg)](https://codecov.io/gh/Clariteia/minos_microservice_saga)\n\n![Tests](https://github.com/Clariteia/minos_microservice_saga/actions/workflows/python-tests.yml/badge.svg)\n\nPython Package for Saga Management in MinOS Microservice Infrastructure\n\nCredits\n-------\n\nThis package was created with ![Cookiecutter](https://github.com/audreyr/cookiecutter)  and the ![Minos Package](https://github.com/Clariteia/minos-pypackage) project template.\n\n\n',
    'author': 'Clariteia Devs',
    'author_email': 'pypi@clariteia.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://clariteia.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

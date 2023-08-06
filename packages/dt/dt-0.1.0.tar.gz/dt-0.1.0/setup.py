# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['dt']
install_requires = \
['ilexconf>=0.9.6,<0.10.0']

setup_kwargs = {
    'name': 'dt',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Vagiz Duseev',
    'author_email': 'vagiz.duseev@dynatrace.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

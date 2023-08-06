# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['shorser']
setup_kwargs = {
    'name': 'shorser',
    'version': '0.1.0',
    'description': 'a shorter serializer',
    'long_description': None,
    'author': 'Cologler',
    'author_email': 'skyoflw@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

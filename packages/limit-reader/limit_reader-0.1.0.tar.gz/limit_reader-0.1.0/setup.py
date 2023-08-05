# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['limit_reader']
setup_kwargs = {
    'name': 'limit-reader',
    'version': '0.1.0',
    'description': 'Limit read size',
    'long_description': None,
    'author': 'Miki Tebeka',
    'author_email': 'miki@353solutions.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

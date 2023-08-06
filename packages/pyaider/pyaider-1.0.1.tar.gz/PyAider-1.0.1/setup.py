# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['pyaider']
setup_kwargs = {
    'name': 'pyaider',
    'version': '1.0.1',
    'description': '',
    'long_description': None,
    'author': 'EGOG',
    'author_email': 'eqqwytyewweqtyeq@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

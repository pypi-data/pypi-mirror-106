# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['tikotmusicaly']
setup_kwargs = {
    'name': 'tikotmusicaly',
    'version': '1.0.0',
    'description': 'View your tracks uploaded on TikOt Musica.ly!',
    'long_description': None,
    'author': 'TikOt Python Library',
    'author_email': 'tikotstudio@yandex.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mst_ssh']
entry_points = \
{'console_scripts': ['mst-ssh = mst_ssh:main']}

setup_kwargs = {
    'name': 'mst-ssh',
    'version': '0.1.0',
    'description': "A command line utility to setup SSH connection to Missouri S&T's Linux virtual machines",
    'long_description': None,
    'author': 'Kevin Lai',
    'author_email': 'zlnh4@umsystem.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

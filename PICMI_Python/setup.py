#!/usr/bin/env python
# To use:
#       python setup.py install

from setuptools import setup

setup(name = 'picmistandard',
      version = '0.0.13',
      description = 'Python base classes for PICMI standard',
      install_requires=['scipy~=1.5'],
      platforms = 'any',
      packages = ['picmistandard'],
      package_dir = {'picmistandard': '.'},
      url = 'https://github.com/picmi-standard/picmi'
      )

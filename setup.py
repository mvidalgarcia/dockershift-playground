# This file is part of dockershift-playground.
# Copyright (C) 2017 CERN
#
# dockershift-playground is free software; you can redistribute it
# and/or modify it under the terms of the Revised BSD License.

from __future__ import unicode_literals


from distutils.core import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()


setup(name='dockershift-playground',
      version='0.0.0',
      url='https://github.com/mvidalgarcia/dockershift-playground',
      packages=find_packages(),
      include_package_data=True,
      install_requires=requirements,
      entry_points={'console_scripts': ['dockershift-playground = app.hello:main']})

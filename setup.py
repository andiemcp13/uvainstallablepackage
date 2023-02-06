#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shared',
      version='6.0.0',
      description='This package has shared components.',
      author='Andie McPartland',
      author_email='amm3hf@virginia.edu',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )

#!/usr/bin/env python

from daemon import version

from pip.req import parse_requirements

from setuptools import find_packages, setup


setup(name='python-daemon',
      version=version.__version__,
      description='Python daemon package.',
      author='Sander Marechal, David Mytton, Pedro Salgado',
      author_email='david@boxedice.com, steenzout@ymail.com',
      packages=find_packages(exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')),
      install_requires=[str(pkg.req) for pkg in parse_requirements('requirements.txt')],
      tests_requires=[str(pkg.req) for pkg in parse_requirements('test-requirements.txt')])

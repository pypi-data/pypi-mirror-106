#!/usr/bin/env python3
# Copyright 2021 Tolteck

import importlib.machinery
import pathlib
import setuptools

path = str(pathlib.Path(__file__).parent.absolute()) + '/couchcopy'
couchcopy = importlib.machinery \
            .SourceFileLoader('couchcopy', path).load_module()

setuptools.setup(
    name='couchcopy',
    version=couchcopy.__version__,
    author='Hoël Iris',
    url='https://github.com/tolteck/couchcopy',
    description='Backup and restore CouchDB cluster',
    long_description=open('README.rst').read(),
    license='GPLv3',
    scripts=['couchcopy'],
    install_requires=['aiocouch >=1.1.0'],
    python_requires='>=3.5',
)

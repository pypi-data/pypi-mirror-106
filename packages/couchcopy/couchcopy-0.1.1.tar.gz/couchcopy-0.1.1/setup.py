#!/usr/bin/env python3
# Copyright 2021 Tolteck

import importlib.machinery
import pathlib
import setuptools

path = str(pathlib.Path(__file__).parent.absolute())
couchcopy = importlib.machinery \
            .SourceFileLoader('couchcopy', path + '/couchcopy.py').load_module()
with open('README.rst', 'r') as f:
    readme = f.read()

setuptools.setup(
    name='couchcopy',
    version=couchcopy.__version__,
    author='Hoël Iris',
    url='https://github.com/tolteck/couchcopy',
    description='Backup and restore CouchDB cluster',
    long_description=readme,
    license='GPLv3',
    py_modules=['couchcopy'],
    entry_points='''
        [console_scripts]
        couchcopy = couchcopy:couchcopy
    ''',
    install_requires=['aiocouch >=1.1.0'],
    python_requires='>=3.5',
)

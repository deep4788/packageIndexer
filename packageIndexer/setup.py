#!/usr/bin/env python

import pind
import os
from setuptools import setup, find_packages

setup(
    name='pind',
    version=pind.__version__,
    description='A package indexer system to keeps track of package dependencies',
    author='Deep Aggarwal',
    author_email='deep.uiuc@gmail.com',
    maintainer='Deep Aggarwal',
    maintainer_email='deep.uiuc@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pind = pind.pind:main',
        ]
    },
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='PENA',
    version='0.1.0',
    description="PENA's an Entirely New Akinator",
    long_description=open('README.md').read(),
    keywords="artificial intelligence prolog game",
    packages=['pena'],
    install_requires=[
        'pyswip_alt==0.2.3', 'flask==0.12.3', 'tinydb==3.5.0', 'jsonschema==2.6.0', 'flask-cors==3.0.3'],
    extras_require={
        'dev': ['pep8'],
    },
    entry_points={
        'console_scripts': [
            'pena=pena.bootstrap:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

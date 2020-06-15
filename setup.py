#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup, Extension

setup(
    name='led-control',
    version='1.0.0',
    description='',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='jackw01',
    python_requires='>=3.7.0',
    url='',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'opencv-python>=4.2.0.34',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'cvtest=cv:main'
        ]
    },
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
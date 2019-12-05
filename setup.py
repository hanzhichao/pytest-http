#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

setup_requirements = ['pytest-runner',]

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Fixture "http" for http requests',
    long_description='Session scope fixture "data" for test from yaml file, '
                     'and function scope "case_data" for this test function',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    license="MIT license",
    include_package_data=True,
    keywords=[
        'pytest', 'py.test', 'http', 'requests'
    ],
    name='pytest-http',
    packages=find_packages(include=['pytest_http']),
    setup_requires=setup_requirements,
    url='https://github.com/hanzhichao/pytest-http',
    version='0.1',
    zip_safe=True,
    install_requires=[
        'pytest',
        'pytest-runner',
        'requests'
    ],
    entry_points={
        'pytest11': [
            'pytest-http = pytest_http.plugin',
        ]
    }
)

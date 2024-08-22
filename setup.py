#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
import os

from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))
setup_requirements = ['pytest-runner', ]


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    description='Fixture "http" for http requests',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
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
    version='0.1.1',
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

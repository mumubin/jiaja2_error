#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='jinja2_error',
    version='0.1.0',
    author='Robin Hu',
    author_email='given.hubin@gmail.com',
    maintainer='Robin Hu',
    maintainer_email='given.hubin@gmail.com',
    license='MIT',
    url='https://github.com/mumubin/jiaja2_error',
    description='Jinja2 Extension for Raise Error',
    long_description=read('README.rst'),
    long_description_content_type='text/x-rst',
    packages=[
        'jinja2_error',
    ],
    package_dir={'jinja2_error': 'jinja2_error'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jinja2',
    ],
    extras_require={
        ":python_version=='2.7'": ["arrow"],
        ":python_version<='3.4'": ["arrow<=0.13.2"],
        ":python_version>='3.5'": ["arrow"]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
    ],
    keywords=['jinja2', 'extension', 'error'],
)

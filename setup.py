# This file is part of Dictdiffer.
#
# Copyright (C) 2013 Fatih Erikli.
# Copyright (C) 2014, 2015, 2016 CERN.
# Copyright (C) 2017, 2019 ETH Zurich, Swiss Data Science Center, Jiri Kuncar.
#
# Dictdiffer is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more
# details.

"""Dictdiffer is a library that helps you to diff and patch dictionaries."""

from __future__ import absolute_import, print_function

from setuptools import find_packages, setup

readme = open('README.rst').read()

tests_require = [
    'pytest-invenio>=1.4.0',
    'mock>=1.3.0',
    'tox>=3.7.0',
]

extras_require = {
    'docs': [
        'Sphinx>=3',
        'sphinx-rtd-theme>=0.2',
    ],
    'numpy': [
        'numpy>=1.11.0',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for key, reqs in extras_require.items():
    if ':' == key[0]:
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'pytest-runner>=2.7',
    'setuptools_scm>=3.1.0',
]

packages = find_packages()

import dictdiffer

setup(
    name='dictdiffer-jira-offline-fork',
    version=dictdiffer.__version__,
    description=__doc__,
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Invenio Collaboration',
    author_email='info@inveniosoftware.org',
    url='https://github.com/mafrosis/dictdiffer',
    project_urls={
        'Changelog': (
            'https://github.com/mafrosis/dictdiffer'
            'blob/master/CHANGES'
        ),
        'Docs': 'https://dictdiffer.rtfd.io/',
    },
    packages=['dictdiffer'],
    zip_safe=False,
    extras_require=extras_require,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
    ],
)

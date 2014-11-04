#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packaging setup for {{ cookiecutter.repo_name }}."""

from {{ cookiecutter.app_name }} import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    'Django>=1.6',
]

test_requirements = [
    'dj_database_url',
    'django_nose',
    'django_extensions',
    'jingo',
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version=version,
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme + '\n\n' + history,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=[
        '{{ cookiecutter.app_name }}',
    ],
    package_dir={
        '{{ cookiecutter.app_name }}': '{{ cookiecutter.app_name }}',
    },
    include_package_data=True,
    install_requires=requirements,
    license="MPL 2.0",
    zip_safe=False,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='{{ cookiecutter.site_name }}.runtests.runtests',
    tests_require=test_requirements
)


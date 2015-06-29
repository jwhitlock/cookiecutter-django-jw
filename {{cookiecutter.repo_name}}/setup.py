#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Packaging setup for {{ cookiecutter.repo_name }}."""

from {{ cookiecutter.app_name }} import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_long_description(title):
    """Create the long_description from other files."""
    readme = open('README.rst').read()
    history = open('HISTORY.rst').read()

    body_tag = ".. Omit badges from docs"
    readme_body_start = readme.index(body_tag)
    assert readme_body_start
    readme_body = readme[readme_body_start + len(body_tag):]

    history_body = history.replace('.. :changelog:', '')
    bars = '=' * len(title)
    long_description = """
%(bars)s
%(title)s
%(bars)s
%(readme_body)s

%(history_body)s
""" % locals()
    return long_description

requirements = [
    'Django>=1.6',
]

test_requirements = [
    'dj_database_url',
    'django_nose',
    'django_extensions',
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version=version,
    description='{{ cookiecutter.project_short_description }}',  # flake8: noqa
    long_description=get_long_description('{{ cookiecutter.project_short_description }}'),
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


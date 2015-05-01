.. {{ cookiecutter.repo_name }} documentation master file, created by
   sphinx-quickstart on Mon Jul 21 13:24:51 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

{{ "=" * cookiecutter.project_short_description|length }}
{{ cookiecutter.project_short_description }}
{{ "=" * cookiecutter.project_short_description|length }}

.. include:: ../README.rst
    :start-after: .. Omit badges from docs

Contents
========

.. toctree::
   :maxdepth: 2

   project
   installation
   usage
   contributing
   authors
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


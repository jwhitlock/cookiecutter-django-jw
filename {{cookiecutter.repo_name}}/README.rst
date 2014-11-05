{% for c in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for c in cookiecutter.project_name %}={% endfor %}

.. This causes warnings from Sphinx due to external images, but the GitHub parser ignores raw HTML

.. image:: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.png?branch=master
    :height: 22px
    :alt: The status of Travis continuous integration tests
    :target: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}

.. image:: https://coveralls.io/repos/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/badge.png?branch=master
    :height: 22px
    :alt: The code coverage
    :target: https://coveralls.io/r/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}?branch=master

.. image:: https://badge.fury.io/py/{{cookiecutter.repo_name}}.png
    :height: 22px
    :alt: The PyPI package
    :target: http://badge.fury.io/py/{{cookiecutter.repo_name}}

.. image:: https://pypip.in/d/{{cookiecutter.repo_name}}/badge.png
    :height: 22px
    :alt: PyPI download statistics
    :target: https://pypi.python.org/pypi/{{cookiecutter.repo_name}}

.. image:: https://www.herokucdn.com/deploy/button.png
    :height: 35px
    :alt: Deploy to Heroku
    :target: https://heroku.com/deploy?template=https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}

{{ cookiecutter.project_short_description }}

* Free software: Mozilla Public License Version 2.0
* Documentation: https://{{ cookiecutter.repo_name }}.readthedocs.org
* Generated from: https://github.com/jwhitlock/cookiecutter-django-jw.git

Features
--------

* TODO

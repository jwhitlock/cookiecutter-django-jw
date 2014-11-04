{% for c in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for c in cookiecutter.project_name %}={% endfor %}

.. Include badges, while avoiding Sphinx "External image" warnings

.. raw:: html

    <p style="height:22px">
      <a href="https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}">
        <img src="https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.png?branch=master"
             alt="The status of Travis continuous integration tests">
      </a>
      <a href="https://coveralls.io/r/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}?branch=master">
        <img src="https://coveralls.io/repos/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/badge.png?branch=master"
             alt="The code coverage">
      </a>
      <a href="http://badge.fury.io/py/{{cookiecutter.repo_name}}">
        <img src="https://badge.fury.io/py/{{cookiecutter.repo_name}}.png"
             alt="The PyPI package">
      </a>
      <a href="https://pypi.python.org/pypi/{{cookiecutter.repo_name}}">
        <img src="https://pypip.in/d/{{cookiecutter.repo_name}}/badge.png"
             alt="PyPI download statistics">
      </a>
    </p>
    <p style="height:35px">
      <a href="https://heroku.com/deploy?template=https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}">
        <img src="https://www.herokucdn.com/deploy/button.png"
             alt="Deploy to Heroku">
      </a>
    </p>


{{ cookiecutter.project_short_description }}

* Free software: Mozilla Public License Version 2.0
* Documentation: https://{{ cookiecutter.repo_name }}.readthedocs.org
* Generated from: https://github.com/jwhitlock/cookiecutter-django-jw.git

Features
--------

* TODO

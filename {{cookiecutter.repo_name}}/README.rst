{% for c in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for c in cookiecutter.project_name %}={% endfor %}

.. Include badges, while avoiding Sphinx "External image" warnings

.. raw:: html

    <p style="height:22px">
      <a href="https://travis-ci.org/jwhitlock/drf-cached-instances">
        <img src="https://travis-ci.org/jwhitlock/drf-cached-instances.png?branch=master"
             alt="The status of Travis continuous integration tests">
      </a>
      <a href="https://coveralls.io/r/jwhitlock/drf-cached-instances?branch=master">
        <img src="https://coveralls.io/repos/jwhitlock/drf-cached-instances/badge.png?branch=master"
             alt="The code coverage">
      </a>
      <a href="http://badge.fury.io/py/drf-cached-instances">
        <img src="https://badge.fury.io/py/drf-cached-instances.png"
             alt="The PyPI package">
      </a>
      <a href="https://pypi.python.org/pypi/drf-cached-instances">
        <img src="https://pypip.in/d/drf-cached-instances/badge.png"
             alt="PyPI download statistics">
      </a>
    </p>
    <p style="height:35px">
      <a href="https://heroku.com/deploy?template=https://github.com/jwhitlock/drf-cached-instances">
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

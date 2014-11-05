About this repository
=====================
This project was created from the cookiecutter-django-jw template, using
a process like this:

.. code-block:: sh

    $ cd ~/src/
    $ cookiecutter https://github.com/jwhitlock/cookiecutter-django-jw.git
    config_path is ~/.cookiecutterrc
    full_name (default is "John Whitlock")? {{ cookiecutter.full_name }}
    email (default is "john@factorialfive.com")? {{cookiecutter.email }}
    github_username (default is "jwhitlock")?  {{cookiecutter.github_username}}
    repo_name (default is "boilerplate")? {{cookiecutter.repo_name}}
    project_name (default is "Python Boilerplate")? {{ cookiecutter.project_name }}
    app_name (default is "boilerplate")? {{ cookiecutter.app_name }}
    site_name (default is "bpsite")? {{ cookiecutter.site_name }}
    project_short_description (default is "Python Boilerplate contains all the boilerplate you need to create a Python package.")? {{ cookiecutter.project_short_description}}
    release_date (default is "2015-01-11")? {{ cookiecutter.release_date }}
    year (default is "2014")? {{ cookiecutter.year }}
    version (default is "0.1.0")? {{ cookiecutter.version }}
    $ cd {{ cookiecutter.repo_name }}
    $ git init
    Initialized empty Git repository in ~/src/{{ cookiecutter.repo_name }}/.git/
    $ git add .
    $ git commit -am "Initial commit"
    [master (root-commit) 75bc198] Initial commit
     61 files changed, 21366 insertions(+)
     create mode 100644 .coveragerc
     create mode 100644 .editorconfig
     create mode 100644 .gitignore
     ...
     create mode 100644 setup.cfg
     create mode 100755 setup.py
     create mode 100644 tox.ini
    $ mkvirtualenv {{ cookiecutter.repo_name }}
    New python executable in {{ cookiecutter.repo_name }}/bin/python2.7
    Also creating executable in {{ cookiecutter.repo_name }}/bin/python
    Installing setuptools, pip...done.
    $ pip install -r requirements.txt
     (development requirements installed)
    $ ./manage.py migrate

Development Features
--------------------
After a basic install, you can run:

* ``make qa`` - runs flake8 for PEP8 and PEP257 compliance checking.  Runs
  coverage to confirm 100% code coverage for the app.
* ``make install_jslint`` - Install node and jslint in the virtualenv.  Future
  runs of ``make qa`` will include jslint checking of project javascript.
* ``make qa-all`` - All the checks of ``make qa``, plus building documentation,
  building and checking packaging, and running tox against a range of Python
  Django versions.
* ``make`` - See other make targets.
* ``./manage.py test`` - Run tests with the nose test runner
* ``./manage.py test --failed --ipdb --ipdb-failures`` - Run tests.  Keep track
  of which tests failed, and only run those in the future.  When an issue
  appears, debug in an interactive ipdb session.
* ``DEBUG=1 ./manage.py runserver_plus`` - Run in debug mode.  Includes Django
  Debug Toolbar for peeking behind the scenes, and interactive tracebacks on
  failures.

Deployment Features
-------------------
{{ cookiecutter.site_name }}/settings.py is built using the 12factor_
principle of getting configuration from the environment.  The default
configuration is release mode.  You'll need to set environment variables
to match your desired configuration.

In development, some ways to set the environment are:

* On the command line: ``DEBUG=1 ./manage.py runserver``
* Export settings: ``export DEBUG=1; ./manage.py runserver``
* As part of virtualenv initialization: ``vim $VIRTUAL_ENV/bin/postactivate``
  for the ``export DEBUG=1`` set statements, and
  ``vim $VIRTUAL_ENV/bin/predeactivate`` for the ``export DEBUG=`` clear
  statements.

Heroku deployment is included.  This can be done with the 'Deploy to Heroku'
button, or manually:


.. code-block:: sh

    $ heroku apps:create {{ cookiecutter.repo_name }}

Then config for development:

.. code-block:: sh

    $ heroku config:set EXTRA_INSTALLED_APPS=gunicorn STATIC_ROOT=static DEBUG=1

Or for production:

.. code-block:: sh

    $ heroku config:set EXTRA_INSTALLED_APPS=gunicorn STATIC_ROOT=static DEBUG=0 ALLOWED_HOSTS={{ cookiecutter.repo_name }}.herokuapp.com SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTOCOL,https

When you've got the app configured, deploy your code to run it:

.. code-block:: sh

    $ git push heroku master
    $ heroku open

.. _12factor: http://12factor.net

Getting rid of this documentation
---------------------------------
Edit or remove "docs/project.rst".  If you remove it, also remove the
"project" line from "docs/index.rst".

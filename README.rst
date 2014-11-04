======================
cookiecutter-django-jw
======================

Cookiecutter template for a Python package or project
See https://github.com/jwhitlock/cookiecutter-django-jw.git

* Free software: Mozilla Public License Version 2.0
* Vanilla testing setup with `unittest` and `python setup.py test`
* Skeleton Django project to support `./manage.py`
* Jinja2 / jingo with Bootstrap 3 for templates
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4
  against Django 1.6 and 1.7
* Sphinx_ docs: Documentation ready for generation with, for example,
  ReadTheDocs_
* Quick quality check with `make qa`, 100% coverage and clean PEP8/PEP257
* Release QA check with `make qa-all`, with clean packaging
  

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/jwhitlock/cookiecutter-django-jw.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis CI account.
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service
  hook.
* Release your package the standard Python way. Here's a release checklist:
  https://gist.github.com/audreyr/5990987

Not Exactly What You Want?
--------------------------

Don't worry, you have options:

Similar Cookiecutter Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `audreyr/cookiecutter-pypackage`_: The original project

* `Nekroze/cookiecutter-pypackage`_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.

* `tony/cookiecutter-pypackage`_: Fork with py2.7+3.3 optimizations. Flask/Werkzeug-style
  test runner, ``_compat`` module and module/doc conventions. See ``README.rst`` or
  the `github comparison view`_ for exhaustive list of additions and modifications.

* Also see the `network`_ and `family tree`_ for audreyr's repo, and many
  projects linked from the cookiecutter_ repo.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Nekroze/cookiecutter-pypackage`: https://github.com/Nekroze/cookiecutter-pypackage
.. _`tony/cookiecutter-pypackage`: https://github.com/tony/cookiecutter-pypackage
.. _github comparison view: https://github.com/tony/cookiecutter-pypackage/compare/audreyr:master...master
.. _`network`: https://github.com/audreyr/cookiecutter-pypackage/network
.. _`family tree`: https://github.com/audreyr/cookiecutter-pypackage/network/members
.. _`cookiecutter`: https://github.com/audreyr/cookiecutter

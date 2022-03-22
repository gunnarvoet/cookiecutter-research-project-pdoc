======================
Cookiecutter Research Project
======================

Cookiecutter_ template for a research project using Python code and Sphinx docs.

* GitHub repo: https://github.com/gunnarvoet/cookiecutter-research-project/
* Free software: BSD license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Sphinx_ docs: Documentation ready for generation with, for example, `Read the Docs`_
* bump2version_: Pre-configured version bumping with a single command
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter


Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install pyyaml
    pip install -U cookiecutter

Generate a Python-based research project::

    cookiecutter https://github.com/gunnarvoet/cookiecutter-research-project.git

Then:

* Install conda environment (``conda env create -f environment.yml``)
* Add a ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files

.. _Sphinx: http://sphinx-doc.org/
.. _bump2version: https://github.com/c4urself/bump2version

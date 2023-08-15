Cookiecutter Research Project
=============================

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a
research project using Python code and [pdoc](https://pdoc.dev/) for API docs.

-   GitHub repo:
    <https://github.com/gunnarvoet/cookiecutter-research-project-pdoc/>
-   Free software: BSD license

# Features

-   Testing setup with `unittest` and `python setup.py test` or `pytest`
-   [pdoc](https://pdoc.dev/) docs: Documentation ready
-   Optionally add custom [pdoc theme](https://github.com/gunnarvoet/pdoc-theme-gv) as git submodule
-   yaml config file (template generated with post hook) with reading
    function in *io*.

# Quickstart

Install the latest Cookiecutter if you haven\'t installed it yet (this
requires Cookiecutter 1.4.0 or higher):
```sh
pip install pyyaml
pip install -U cookiecutter
```

Generate a Python-based research project:
```sh
cookiecutter https://github.com/gunnarvoet/cookiecutter-research-project-pdoc.git
```

Then:

-   Install the conda environment
    (`conda env create -f environment.yml`)
-   Install additonal packages like jupyter notebook. Gunnar installs
    these using pip and a *requirements.txt* file and has a little
    script that just does this. This way non-essential packages are kept
    outside the *environment.yml* for this package.

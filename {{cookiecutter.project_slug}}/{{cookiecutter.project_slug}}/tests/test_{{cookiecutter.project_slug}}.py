#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

import {{ cookiecutter.project_slug }}

def test_read_config():
    cfg = {{ cookiecutter.project_slug }}.io.load_config()
    assert isinstance(cfg, dict)


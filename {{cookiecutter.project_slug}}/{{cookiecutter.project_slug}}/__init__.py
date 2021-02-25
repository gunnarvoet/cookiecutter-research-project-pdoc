"""Top-level package for {{ cookiecutter.project_name }}."""

__author__ = """{{ cookiecutter.full_name }}"""
__email__ = '{{ cookiecutter.email }}'
__version__ = '{{ cookiecutter.version }}'

__all__ = ["io", "{{cookiecutter.project_slug}}"]
from . import io, {{cookiecutter.project_slug}}

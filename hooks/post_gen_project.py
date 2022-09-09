#!/usr/bin/env python
import os
from pathlib import Path
import yaml

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
parent = Path(PROJECT_DIRECTORY).parent


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def generate_cfg_file():
    path = dict(
        path = dict(
            root = PROJECT_DIRECTORY,
            proc = parent.joinpath('data').as_posix(),
            data = 'data/',
            fig = 'fig/',
        )
    )
    data = dict(
            instrument_type = dict(mooring_name='$proc/path/to/processed/file.nc')
            )
    with open('config.yml', 'w') as outfile:
        yaml.dump(path, outfile, default_flow_style=False)
        yaml.dump(data, outfile, default_flow_style=False)


if __name__ == '__main__':

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    generate_cfg_file()

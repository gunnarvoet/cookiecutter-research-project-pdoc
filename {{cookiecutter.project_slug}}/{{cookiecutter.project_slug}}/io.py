#!/usr/bin/env python
# coding: utf-8
"""
Read and write data.
"""

from pathlib import Path
import collections.abc
import yaml
from box import Box
import matplotlib.pyplot as plt

import gvpy as gv


def load_config() -> Box:
    """Load the yaml config file.

    Returns
    -------
    cfg : Box
        Config parameters dictionary with dot access.
    """

    def find_config_file():
        # first look in current directory
        cwd = Path(".").absolute()
        files = list(cwd.glob("config.yml"))
        if len(files) == 1:
            cfile = files[0]
        else:
            # otherwise go through parent directories
            parents = list(Path.cwd().parents)
            for pi in parents:
                files = list(pi.glob("config.yml"))
                if len(files) == 1:
                    cfile = files[0]
        return cfile

    configfile = find_config_file()
    with open(configfile, "r") as ymlfile:
        cfg = Box(yaml.safe_load(ymlfile))
    cfg.path.root = configfile.parent

    # Convert paths to Path objects
    cfg.path.data = cfg.path.root.joinpath(cfg.path.data)
    cfg.path.fig = cfg.path.root.joinpath(cfg.path.fig)

    def replace_variables(dict_in, var, rootpath):
        d = dict_in.copy()
        n = len(var)
        for k, v in d.items():
            if isinstance(v, collections.abc.Mapping):
                d[k] = replace_variables(d.get(k, {}), var, rootpath)
            elif isinstance(v, str):
                if v.startswith(var + "/"):
                    d[k] = rootpath.joinpath(v[n + 1 :])
            else:
                d[k] = v
        return d

    # Replace variables from the yaml file.
    cfg = replace_variables(cfg, "$data", cfg.path.data)

    return cfg


def print_config(print_values=False):
    """Pretty print project configuration.

    Parameters
    ----------
    print_values : bool, optional
        Show values (instead of keys only).
    """

    cfg = load_config()
    gv.misc.pretty_print(cfg, print_values=print_values)


def png(fname, subdir=None, **kwargs):
    """Save figure as png to the figure path defined in config.yml.

    Parameters
    ----------
    fname : str
        Figure name without file extension.
    subdir : str, optional
        Save figure to this subdirectory within the project figure directory.
    """
    cfg = load_config()
    if subdir is not None:
        figdir = cfg.path.fig.joinpath(subdir)
    else:
        figdir = cfg.path.fig
    gv.plot.png(fname, figdir=figdir, **kwargs)


def pdf(fname, subdir=None):
    """Save figure as pdf to the figure path defined in config.yml.

    Parameters
    ----------
    fname : str
        Figure name without file extension.
    subdir : str, optional
        Save figure to this subdirectory within the project figure directory.
    """
    fname = fname + ".pdf"
    cfg = load_config()
    if subdir is not None:
        figdir = cfg.path.fig.joinpath(subdir)
        figdir.mkdir(exist_ok=True)
    else:
        figdir = cfg.path.fig
    print("saving pdf to {}/".format(figdir))
    plt.savefig(figdir.joinpath(fname), bbox_inches="tight", dpi=200)

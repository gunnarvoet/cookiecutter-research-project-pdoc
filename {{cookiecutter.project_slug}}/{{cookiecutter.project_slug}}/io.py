#!/usr/bin/env python
# coding: utf-8
"""
Read and write data.
"""

from pathlib import Path
import os
import yaml
from box import Box
import warnings

import gvpy as gv

warnings.filterwarnings("ignore", message="Mean of empty slice")


def load_config() -> Box:
    """Load the yaml config file.

    Returns
    -------
    cfg : Box
        Config parameters dictionary with dot access.
    """
    try:
        configfile = Path("config.yml")
        assert configfile.exists()
    except AssertionError:
        try:
            configfile = Path("../config.yml")
            assert configfile.exists()
        except AssertionError:
            try:
                configfile = Path("../../config.yml")
                assert configfile.exists()
            except AssertionError:
                cwd = os.getcwd()
                print(f"cannot locate config.yml in {cwd} or its parent directory")
                return
    with open(configfile, "r") as ymlfile:
        cfg = Box(yaml.safe_load(ymlfile))
    # Convert paths to Path objects
    cfg.path.root = Path(cfg.path.root)
    cfg.path.data = cfg.path.root.joinpath(cfg.path.data)
    cfg.path.fig = cfg.path.root.joinpath(cfg.path.fig)

    # # Construct paths for obs output
    # for k, v in cfg.obs.output.items():
    #     cfg.obs[k] = cfg.path.data.joinpath(v)
    # # Construct paths for model output
    # for k, v in cfg.model.output.items():
    #     cfg.model[k] = cfg.path.data.joinpath(v)

    return cfg


def png(fname, **kwargs):
    """Save figure as png to the path defined in config.yml.
    Parameters
    ----------
    fname : str
        Figure name without file extension.
    """
    cfg = load_config()
    gv.plot.png(fname, figdir=cfg.path.fig)

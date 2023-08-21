# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.0
#   kernelspec:
#     display_name: Python [conda env:{{ cookiecutter.project_slug }}]
#     language: python
#     name: conda-env-{{ cookiecutter.project_slug }}-py
# ---

# %% [markdown] heading_collapsed=true
# #### Imports

# %% hidden=true
# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import xarray as xr
import gsw

import gvpy as gv

import {{ cookiecutter.project_slug }}

# %reload_ext autoreload
# %autoreload 2

# %config InlineBackend.figure_format = 'retina'

# %% hidden=true
cfg = {{ cookiecutter.project_slug }}.io.load_config()

# %% [markdown]
# # Title

# %%

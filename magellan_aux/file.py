"""
Common file handling operations when working with Magellan.
"""

import glob

import pandas as pd


def concatenate(glob_expr, dtype={}, ignore_index=False):
    datasets = [pd.read_csv(path, dtype=dtype) for path in glob.glob(glob_expr)]
    return pd.concat(datasets, ignore_index=ignore_index).drop_duplicates()

"""
Set up metadata for files involved in matching.
"""

import pandas as pd
import py_entitymatching as em


def read_pair_csv_with_metadata(
        pair_filename, tuple_filename,
        pairs_key, tuples_key,
        pair_dtype={}, tuple_dtype={}
    ):
    # Way to inject dtype parameter into native? For now, do it "by hand"
    pairs = pd.read_csv(pair_filename, dtype=pair_dtype)
    tuples = pd.read_csv(tuple_filename, dtype=tuple_dtype)
    em.set_key(pairs, pair_key)
    em.set_key(tuples, tuple_key)
    em.set_ltable(pairs, tuples)
    em.set_fk_ltable(pairs, f'ltable_{tuple_key}')
    em.set_rtable(pairs, tuples)
    em.set_fk_rtable(pairs, f'rtable_{tuple_key}')
    return pairs, tuples
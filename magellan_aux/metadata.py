"""
Set up metadata for files involved in matching.
"""

import pandas as pd
import py_entitymatching as em


def read_tuple_csv_with_metadata(filename, key, dtype={}):
    # Way to inject dtype parameter into native? For now, do it "by hand"
    tuples = pd.read_csv(filename, dtype=dtype)
    em.set_key(tuples, key)
    return tuples


def read_pair_csv_with_metadata(tuples, filename, key, dtype={}):
    # Way to inject dtype parameter into native? For now, do it "by hand"
    pairs = pd.read_csv(filename, dtype=dtype)
    em.set_key(pairs, key)
    em.set_ltable(pairs, tuples)
    em.set_fk_ltable(pairs, f'ltable_{em.get_key(tuples)}')
    em.set_rtable(pairs, tuples)
    em.set_fk_rtable(pairs, f'rtable_{em.get_key(tuples)}')
    return pairs
"""
Functions to help write features.
"""

# Normalization

def ascii_uppercase_alphanum(s, decoding='utf-8'):
    """Convert a string to alphanumeric ASCII uppercase characters."""
    if type(s) is float:
        return s
    nfkd = unicodedata.normalize('NFKD', s)
    only_ascii = nfkd.encode('ASCII', 'ignore')
    upper = only_ascii.upper()
    decoded = upper.decode(decoding)
    alphanum = ' '.join(m.group(0) for m in re.finditer('[A-Z0-9]+', decoded))
    return alphanum

# Feature decorators

def unpack(l_attr, r_attr):
    def decorator(func):
        def unpacked(ltuple, rtuple):
            return func(ltuple[l_attr], rtuple[r_attr])
        return unpacked
    return decorator

def is_null(val):
    return val is None or (type(val) in {float, np.float64} and np.isnan(val))

def non_null_args(default=None):
    def decorator(func):
        def ensure_non_null_args(*vals):
            if any(map(is_null, vals)):
                return default
            return func(*vals)
        return ensure_non_null_args
    return decorator

def preprocess_args(*preprocessing):
    def decorator(func):
        def preprocessed(*args):
            for preprocess_step in preprocessing:
                args = map(preprocess_step, args)
            return func(*args)
        return preprocessed
    return decorator
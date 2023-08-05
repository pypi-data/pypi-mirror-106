import numpy as np
from math import ceil

from Alexandria.math.units import get_representative_decimals


"""
Slicing
"""


def find_nearest_entry(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx, array[idx]


"""
Characteristics
"""


def span(a):
    a_s = a + a.min() if a.min() < 0 else a
    return max(a_s) - min(a_s)


def internal_array_shape(x):
    return np.array([x[n].shape for n in range(len(x))])


"""
Manipulations
"""


def dx_v(t):
    """
    :return: Return vector of base dimension increments, where the base dimension is X in
                    f(X)
             for higher precision differentiation or integration with uneven measurements.
    """
    dt_v = np.array(list([t[i + 1] - t[i]] for i in range(t.size - 1)))
    dt_v = np.append(dt_v, np.array([t[-2] - t[-1]]))
    return dt_v


"""
Console output
"""


def pretty_array(a):
    return np.array2string(a, precision=get_representative_decimals(np.min(a[np.nonzero(a)])), suppress_small=True)


"""
Creation
"""


def lists_to_ndarrays(*args):
    """
    Transform a series of lists into NumPy arrays, and return them contained in a parent NumPy array
    :param args: Number n of lists
    :return: Array of NumPy arrays
    """
    import inspect
    args, _, _, values = inspect.getargvalues(inspect.currentframe())
    inputs = np.array(values["args"], dtype=object).squeeze()
    # inputs = list(values["args"])
    for i in range(len(inputs)):
        if isinstance(inputs[i], np.ndarray):
            pass
        else:
            inputs[i] = np.array(inputs[i])
    return inputs
import numpy as np
from math import ceil


# Angles
def deg(a):
    return a/np.pi*180


def rad(a):
    return a/180*np.pi


# Mass
def lbs_to_kg(m):
    return m*0.453592


"""
Utilities
"""


def get_representative_decimals(n, precision=1/100):
    d = -np.log10(abs(n)*precision)
    return ceil(d) if d > 0 else 0

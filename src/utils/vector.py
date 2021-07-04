"""Core module for vector related operations"""
from pydantic import conlist, confloat

from typing import Dict


def cross(a: conlist(item_type=confloat(),
                     min_items=3,
                     max_items=3),
          b: conlist(item_type=confloat(),
                     min_items=3,
                     max_items=3)) -> Dict[str, float]:
    """Calculate cross production between two vectors"""

    i = a[1] * b[2] - a[2] * b[1]
    j = a[2] * b[0] - a[0] * b[2]
    k = a[0] * b[1] - a[1] * b[0]

    return {
        'x': i,
        'y': j,
        'z': k
    }

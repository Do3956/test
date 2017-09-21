# encoding: utf-8

"""
@version: v1.0
@author: do
@time: 2017/9/19 22:35

使用array比不使用更慢
"""
from __future__ import division
import numpy as np
cimport numpy as np
DTYPE = np.int


def test_list(int x, int y):
    cdef np.ndarray a = np.zeros([], dtype=DTYPE)

    np.append(a, x)
    np.append(a, y)

    return a
# encoding: utf-8

"""
@version: v1.0
@author: do
@time: 2017/9/19 22:35

使用array比不使用更慢
"""

from cpython cimport array
# import array


def test_list(int x, int y):
    # cdef array.array a = array.array('i', [])
    a = []
    a.append(x)
    a.append(y)
# encoding: utf-8

"""
@version: v1.0
@author: do
@time: 2017/9/19 22:35

即时是数据量大的情况下
使用array也比不使用更慢
"""

from cpython cimport array


def test_list(int x, int y):
    cdef array.array a = array.array('i', [])
    a = []

    for i in range(10000):
        a.append(x)
        a.append(y)

    return a
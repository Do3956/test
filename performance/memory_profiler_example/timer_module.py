# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/9/12'
__content__ = ''
"""
import timeit
from functools import wraps


def cul_time_timeit(func):
    # @wraps(func)
    def newFunc(*args, **kwargs):
        t1 = timeit.Timer(func, *args, **kwargs)
        print(t1.timeit())
    return newFunc


@cul_time_timeit
def test():
    # pass
    for i in range(0, 1):
        i = 1

test()
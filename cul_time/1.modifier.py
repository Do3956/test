# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/24'
__content__ = ''
"""
import time
from functools import wraps

def time_fn(fn):
    @wraps(fn)
    def messure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print "use", t2 - t1, "seconds."
        return result
    return messure_time


@time_fn
def test():
    for i in range(5000):
        z = i ** i

test()
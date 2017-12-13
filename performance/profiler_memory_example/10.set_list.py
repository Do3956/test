# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/11'
__content__ = ''
"""

import time
from memory_profiler import profile

@profile
def my_func():
    a=list(xrange(100))
    b=set(a)
    a2 = list(xrange(1000))
    b2 = set(a2)
    a3 = list(xrange(10000))
    b3 = set(a3)
    a3 = list(xrange(100000))
    b3 = set(a3)

if __name__ == '__main__':
    my_func()

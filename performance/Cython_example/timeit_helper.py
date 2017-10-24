# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/9/13'
__content__ = ''
"""

import timeit
from performance.Cython_example import test_1

def run_times():
    for i in range(1):
        test_1.act([3,8],5,1)

print(timeit.timeit(run_times, number=1000000))
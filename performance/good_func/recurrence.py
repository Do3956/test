# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/9/12'
__content__ = '斐波那契数列，递归调用，计算过程递归, 树形分散，指数型增长'
"""
# from memory_profiler import profile


count_times = 0
# @profile(precision=4)
def fb(n):
    global count_times
    count_times += 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fb(n-1) + fb(n-2)

print(fb(10), count_times)
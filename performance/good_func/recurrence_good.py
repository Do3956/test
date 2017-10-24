# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/9/12'
__content__ = '斐波那契数列，递归调用，计算过程迭代'
"""


count_times = 0
def fb(n):
    return fb_item(1, 0, n)

def fb_item(a, b, count):
    global count_times
    count_times += 1

    if count == 0:
        return b

    return fb_item(a+b, a, count-1)

print(fb(10), count_times)
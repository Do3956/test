# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/10/13'
__content__ = ''
"""


def a(target):

    print target.__name__

@a
def b_123(test):
    print test


print a(123)
# print a.__name__
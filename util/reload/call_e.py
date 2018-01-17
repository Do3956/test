# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = ''
"""

class Prod(object):
    def __init__(self, data):
        self.data = data

    def __call__(self, data):
        return self.data * data

X = Prod(10)
print X
print X(2)
print X(3)
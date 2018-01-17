# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = ''
"""


class adder:
    def __init__(self, value=0):
        self.data = value

    def __add__(self, other):
        self.data += other


class addrepr(adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data


x = addrepr(2)  # run __init__
x + 1  # run __add__
print x  # run __repr__
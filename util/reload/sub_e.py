# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = '运算符重载
加法重载
'
"""


class Number:
    def __init__(self, start):
        self.data = start

    def __sub__(self, other):  # minus method
        return Number(self.data - other)

    def __reduce__(self, other):  # minus method
        return Number(self.data - other)


if __name__ == "__main__":
    number = Number(20)
    y = number - 10  # invoke __sub__ method
    print y
    print number - 10

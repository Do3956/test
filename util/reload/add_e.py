# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = '运算符重载
加法重载
'
"""

class myNumber:
    def __init__(self, start):
        self.data = start
    def __str__(self):
        # return str(float(self.data))
        return str(self.data)
    def __add__(self, other):
        return myNumber(self.data + other)
    def __radd__(self, other):
        return myNumber(self.data + other)


if __name__ == "__main__":
    a = myNumber(1)
    b = myNumber(2)

    print "a+1",a+1
    print "1+a",1+a
    print "b+1",b+1
    print "1+b",1+b
    print "a+b",a+b
    print "b+a",b+a

    print str(a)

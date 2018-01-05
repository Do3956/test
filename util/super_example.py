# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/3'
__content__ = ''
"""


class Base(object):
    def __init__(self):
        print 'Base create'


class childA(Base):
    def __init__(self):
        print 'creat A ',
        Base.__init__(self)

class childB(Base):
    def __init__(self):
        print 'creat B ',
        super(childB, self).__init__()

class childC(Base):
    def __init__(self):
        print 'creat C ',

class childD(Base):
    print 'creat D ',
    def a(self):
        pass


base = Base()

a = childA()
b = childB()
c = childC()
d = childD()
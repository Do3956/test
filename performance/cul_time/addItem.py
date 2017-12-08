# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/11/30'
__content__ = ''
"""
import time

def test1(n=1):
    l = []
    for i in xrange(n*10000):
        l = l + [i]
    return l

def test2(n=1):
    l = []
    for i in xrange(n*10000):
        l.append(i)
    return l

def test3(n=1):
    return [i for i in xrange(n*10000)]

def test4(n=1):
    return list(xrange(n*10000))

a = time.time()
test1()
print time.time() - a

a = time.time()
test2(10)
print time.time() - a

a = time.time()
test3(10)
print time.time() - a

a = time.time()
test4(10)
print time.time() - a

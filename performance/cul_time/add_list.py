# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/12'
__content__ = ''
"""
import time

a = []
for i in xrange(1000):
    a.append([i])

start = time.clock()
b = []
for i in xrange(1000):
    b.extend(a[i])

print time.clock()-start

start = time.clock()
b = []
for i in xrange(1000):
    b.extend(a[i])

print time.clock() - start

# print b
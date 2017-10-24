# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/29'
__content__ = 'dict查询key用的是hash，复杂度为O(1);
                list则是一个个查询判断，复杂度为O(n);
                set 查询key用的是__eq__这个magic方法，复杂度为O(1);
                tuple 比list还慢。。。
"""
import time

t1 = time.time()
_dict = {}
for i in xrange(1000000):
    _dict[i] = 1

print 'create dict',time.time() - t1

t1 = time.time()
_list = []
for i in xrange(1000000):
    _list.append(i)
print 'create list',time.time() - t1

_set = set()
t1 = time.time()
for i in xrange(1000000):
    _set.add(i)
print 'create _set',time.time() - t1

t1 = time.time()
if 99999999 in _dict:
    print 1

print 'dict search', time.time() - t1
t1 = time.time()

if 99999999 in _list:
    print 1

print 'list search', time.time() - t1
t1 = time.time()

if 99999999 in _set:
    print 1

print 'set search', time.time() - t1

t1 = time.time()
if 99999999 in tuple(_list):
    print 1

print 'tuple search', time.time() - t1
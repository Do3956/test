# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/29'
__content__ = 'dict查询key用的是hash，复杂度为O(1);
                list则是一个个查询判断，复杂度为O(n);
                set查询key用的是__eq__这个magic方法，复杂度为O(1);'
"""
import time

t1 = time.time()

_dict = {}
_list = []
for i in xrange(9999999):
    _dict[i] = 1
    _list.append(i)

_set = set(_list)

print time.time() - t1
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
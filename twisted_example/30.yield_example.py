# -*- coding: utf-8 -*-
"""
__author__ = 'admin'
__mtime__ = '2017/6/30'
__content__ = ''
"""

def my_generator():
    print 'starting up'
    yield 1
    print "working"
    yield 2
    print "still working"
    yield 3
    print 'done'

for n in my_generator():
    print '----'
    print n
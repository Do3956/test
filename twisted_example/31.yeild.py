# -*- coding: utf-8 -*-
"""
__author__ = 'admin'
__mtime__ = '2017/7/3'
__content__ = ''
"""

def my_generator():
    print 'starting up'
    yield 1
    print "workin'"
    yield 2
    print "still workin'"
    yield 3
    print 'done'

gen = my_generator()

while True:
    try:
        print '-----'
        n = gen.next()
    except StopIteration:
        break
    else:
        print n
# -*- coding: utf-8 -*-
"""
__author__ = 'admin'
__mtime__ = '2017/6/30'
__content__ = ''
"""
class Malfunction(Exception):
    print 'Malfunction',Exception
    pass

def my_generator():
    print 'starting up'

    val = yield 1
    print 'got:', val

    val = yield 2
    print 'got:', val

    try:
        yield 3
    except Malfunction:
        print 'except malfunction!'

    yield 4

    print 'done'

gen = my_generator()

print gen.next() # start the generator
print gen.send(10) # send the value 10
print gen.send(20) # send the value 20
print gen.throw(Malfunction())
 # raise an exception inside the generator

try:
    gen.next()
except StopIteration:
    print 'StopIteration'
# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/26 18:39
"""
import time

@profile
def test():
    for i in xrange(1000):
        i = i ** i
    sleep()
    test1()

def test1():
    sleep()

def sleep():
    time.sleep(1)


test()

_sys = 'python '
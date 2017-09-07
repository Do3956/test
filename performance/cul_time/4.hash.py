# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/29'
__content__ = '生存期内可变的对象不可以哈希,就是说改变时候其id()是不变的'
"""

a= [0,0,0]
b = {1:2,'c':9}
c = set(a)
string = 'hello'

class A():
    pass
a = A()

# print hash(A)
# print hash(a)
# print hash(string)
#
# print hash(c) #不可被hash
# print hash(b) #不可被hash
# print hash(a)
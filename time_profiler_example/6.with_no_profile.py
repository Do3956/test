# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/26 19:43

使用单元测试时，profile报错的解决方案
"""
import unittest

if '__builtin__' not in dir() or not hasattr(__builtin__, 'profile'):
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner

@profile
def some_fn(n):
    return n * 2

class TestCase(unittest.TestCase):
    def test(self):
        result = some_fn(2)
        self.assertEqual(result, 4)

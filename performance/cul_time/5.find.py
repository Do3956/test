# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/11'
__content__ = ''
"""
import time
import random

num = 100000
a = list(xrange(num))
b = list()
t = time.time()

a.sort()

print time.time() -t

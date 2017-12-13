# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/11'
__content__ = ''
"""
import time

num = 10000000
t = time.time()

for i in xrange(num):
    # i % 1 == 0 # 1.02600002289
    # i % 1 # 0.854999780655
    # a = i % 1 # 1.18099999428
    # i > 1 # 0.738999843597
    i < 1000000 and i>100 # 0.946000099182


print time.time() -t

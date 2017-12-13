# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/8'
__content__ = ''
"""

import time

num = 10000000
t = time.time()

for i in range(num):
    pass
print 'range',time.time() - t, num/(time.time() - t)
#range 0.582000017166 17182130.0774

t = time.time()

for i in xrange(num):
    pass
print 'xrange',time.time() -t, num/(time.time() - t)
#xrange 0.392000198364 25510191.1727


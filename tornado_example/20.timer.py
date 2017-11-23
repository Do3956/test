# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/11/20'
__content__ = '异步调用'
"""
import time
import tornado
from tornado import gen
from tornado.ioloop import IOLoop

def do_something():
    print 1111, time.time()
    # time.sleep(0.5)
    time.sleep(0.8)
    print time.time()



tornado.ioloop.PeriodicCallback(do_something, 1000).start()  # start scheduler

IOLoop.instance().start()


#coding:utf8
"""
进程阻塞
"""

import time
import requests


def hello(name):
    print("Hello world!===>" + name + '===>' + str(int(time.time())))


def request_google():
    res = requests.get('http://www.google.com')
    return res

from twisted.internet import reactor, task

reactor.callWhenRunning(hello, 'yudahai')

#google无法访问，超成阻塞
reactor.callLater(1, request_google)

reactor.callLater(3, hello, 'yuyue')

reactor.run()
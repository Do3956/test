# coding:utf-8
"""
进程阻塞 解决方法2
多线程
"""
import time
import requests
from twisted.internet import reactor, task, defer


def hello(name):
    print("Hello world!===>" + name + '===>' + str(int(time.time())))


def request_google():
    try:
        hello('request_google start...')
        result = requests.get('http://www.google.com', timeout=10)
    except Exception as e:
        print e
        return
    print(result)
    hello('request_google end...')


reactor.callWhenRunning(hello, 'yudahai')

reactor.callInThread(request_google)

reactor.callLater(3, hello, 'yuyue')

reactor.run()
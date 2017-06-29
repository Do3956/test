# coding:utf-8
"""
进程阻塞 解决方法1
twisted自带的httpclient进行访问，twisted自带的httpclient由于是异步的，不会阻塞住整个reactor的运行
"""

import time
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet import reactor, task, defer


def hello(name):
    print("Hello world!===>" + name + '===>' + str(int(time.time())))


@defer.inlineCallbacks
def request_google():
    agent = Agent(reactor)
    try:
        hello('request_google start...')
        result = yield agent.request('GET', 'http://www.google.com', Headers({'User-Agent': ['Twisted Web Client Example']}), None)
    except Exception as e:
        print e
        return
    print(result)
    hello('request_google end...')



reactor.callWhenRunning(hello, 'yudahai')

reactor.callLater(1, request_google)

reactor.callLater(3, hello, 'yuyue')

reactor.run()
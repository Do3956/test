# coding:utf-8
"""
进程阻塞 解决方法1
twisted自带的httpclient进行访问，twisted自带的httpclient由于是异步的，不会阻塞住整个reactor的运行
"""

import time
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet import reactor, task
from twisted.internet.defer import inlineCallbacks, Deferred, returnValue


def hello(name):
    print("Hello world!===>" + name + '===>' + str(int(time.time())))


@inlineCallbacks
def request_google():
    agent = Agent(reactor)
    try:
        hello('request_google start...')
        # result = yield agent.request('GET', 'http://www.google.com', Headers({'User-Agent': ['Twisted Web Client Example']}), None)
        result = yield agent.request('GET', 'http://www.baidu.com', Headers({'User-Agent': ['Twisted Web Client Example']}), None)
        returnValue(result)

    except Exception as e:
        print e
        return
    # print(result)
    hello('request_google end...')



reactor.callWhenRunning(hello, 'yudahai')

# print 11111 ,reactor.callLater(1, request_google)
print 2222,request_google()

reactor.callLater(2, hello, 'yuyue')

reactor.run()
# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/31'
__content__ = '不计算消息返回，只关心发送时间
1秒5000次'
"""

import time
from twisted.internet.defer import inlineCallbacks, Deferred, returnValue
from twisted.web import client

from twisted.internet import reactor, defer


def getUrl(url):
    d = client.getPage(url, timeout=5)
    d.addCallback(getResult)


@defer.inlineCallbacks
def getRemoteData(url):
    r1 = yield getUrl(url)
    returnValue(r1)


def getResult(v):
    print time.time(),"result=", type(v),len(v)


start = time.time()
for i in xrange(500):
    getRemoteData('http://www.baidu.com')
print time.time() - start #0.1秒


if __name__ == "__main__":
    reactor.run()

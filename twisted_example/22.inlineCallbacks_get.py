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
    print time.time(),'d',d
    return d

@defer.inlineCallbacks
def getRemoteData(url):
    r1 = yield getUrl(url)
    print time.time(), 'r1',r1
    defer.returnValue(r1)


def getResult(v):
    print time.time(),"result=", type(v),len(v)
    return 'hahhahahah'


# 最终必须要以 getRemoteData 必须也是被 inlineCallbacks 包装的函数，才能对返回值进行进一步的处理，最终在外层被twisted取值给客户端
# a = getRemoteData('http://www.baidu.com')
# print time.time(), 'a',a


if __name__ == "__main__":
    reactor.run()

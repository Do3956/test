import time
import urllib2,urllib
from twisted.internet.defer import inlineCallbacks, Deferred, returnValue
from twisted.web import client

from twisted.internet import reactor, defer


def getUrl():
    # return urllib.urlopen('http://www.baidu.com').read()
    #return urllib2.urlopen('http://www.baidu.com', timeout=5).read()
    d = client.getPage("www.baidu.com")
    d.addCallback(getResult)


@defer.inlineCallbacks
def getRemoteData():
    r1 = yield getUrl()
    returnValue(r1)


def getResult(v):
    # print "result=", v
    d = client.getPage("www.163.com")
    d.addCallback(callback_163)
    return 1

def callback_163():
    pass

if __name__ == '__main__':
    d = getRemoteData()
    d.addCallback(getResult)
    print d


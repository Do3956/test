import time
import urllib2,urllib
from twisted.internet.defer import inlineCallbacks, Deferred, returnValue
from twisted.web import client

from twisted.internet import reactor, defer

def hello(name):
    print("Hello world!===>" ,name, '===>', str(int(time.time())))

def getUrl(url):
    # return urllib2.urlopen(url, timeout=3).read()
    return client.getPage(url, timeout=5)

@defer.inlineCallbacks
def getRemoteData(url):
    r1 = yield getUrl(url)
    # r1.addCallback(getResult)
    hello(r1)
    returnValue(r1)


def getResult(v):
    print "result=", v
    return 1


# if __name__ == '__main__':
#     print time.time()
#     d = getRemoteData('http://101.210.1.13/mormhweb/')
#     print d, time.time()
#     d.addCallback(getResult)
#     print 'addCallback',d, time.time()
#     d = getRemoteData('https://www.blogger.com/blogger.g?blogID=3420102001624496654#allposts')
#     print d, time.time()
#     d.addCallback(getResult)
#     print 'addCallback',d, time.time()

reactor.callWhenRunning(hello, 'yudahai')

d = getRemoteData('http:///www.baidu.com')
print 111111111
hello(d)
d.addCallback(getResult)
print 22222
hello(d)
# print reactor.callLater(1, getRemoteData, 'http://101.210.1.13/mormhweb/')

reactor.callLater(2, hello, 'yuyue')

reactor.run()
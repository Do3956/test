import time
import urllib2,urllib
from twisted.internet.defer import inlineCallbacks, Deferred, returnValue
from twisted.web import client

from twisted.internet import reactor, defer

def hello(name):
    print("Hello world!===>" ,name, '===>', str(int(time.time())))

def getUrl(url):
    return client.getPage(url, timeout=5)

@defer.inlineCallbacks
def getRemoteData(url):
    r1 = yield getUrl(url)
    hello(r1)
    returnValue(r1)


def getResult(v):
    print "result=", v
    return 1


if __name__ == '__main__':
    a = time.time()
    print time.time() - a

    reactor.run()
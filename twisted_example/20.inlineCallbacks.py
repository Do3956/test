import time

from twisted.internet.defer import inlineCallbacks, Deferred, returnValue
from twisted.python.failure import Failure

from twisted.internet import reactor, defer


def loadRemoteData(callback):
    print 111,'loadRemoteData',time.time()
    time.sleep(1)
    print 222,'loadRemoteData',time.time()
    callback(1)
    print 333,'loadRemoteData', time.time()



def loadRemoteData2(callback):
    print 111,'loadRemoteData2',time.time()
    time.sleep(1)
    print 222,'loadRemoteData2',time.time()
    callback(2)
    print 333, 'loadRemoteData2', time.time()


@defer.inlineCallbacks
def getRemoteData():
    d1 = defer.Deferred()
    print 1, 'getRemoteData', time.time()
    reactor.callInThread(loadRemoteData, d1.callback)
    print 2, 'getRemoteData', time.time()
    r1 = yield d1
    print 3, 'getRemoteData', time.time()

    d2 = defer.Deferred()
    print 4, 'getRemoteData', time.time()
    reactor.callInThread(loadRemoteData2, d2.callback)
    print 5, 'getRemoteData', time.time()
    r2 = yield d2
    print 6, 'getRemoteData', time.time()

    returnValue(r1 + r2)

    print 7, 'getRemoteData', time.time()


def getResult(v):
    print "result=", v


if __name__ == '__main__':
    d = getRemoteData()
    d.addCallback(getResult)

    d2 = getRemoteData()
    rst = d2.addCallback(getResult)
    print type(rst), rst

    reactor.callLater(4, reactor.stop);
    reactor.run()  
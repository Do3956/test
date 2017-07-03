# -*- coding: utf-8 -*-
"""
__author__ = 'admin'
__mtime__ = '2017/6/30'
__content__ = ''
"""
import time
from twisted.internet.defer import inlineCallbacks, Deferred
from twisted.internet import reactor


@inlineCallbacks
def my_callbacks():

    print time.time(), 'first callback'
    result = yield 1
    # yielded values that aren't deferred come right back

    print time.time(), 'second callback got', result
    d = Deferred()
    reactor.callLater(2, d.callback, 2)
    result = yield d
    # yielded deferreds will pause the generator

    print time.time(), 'third callback got', result
    # the result of the deferred

    d = Deferred()
    reactor.callLater(2, d.errback, Exception(3))

    try:
        print 111,result
        yield d
    except Exception, e:
        result = e
        print 'Exception',e

    print time.time(), 'fourth callback got', repr(result)
    # the exception from the deferred
    reactor.stop()

reactor.callWhenRunning(my_callbacks)
reactor.run()

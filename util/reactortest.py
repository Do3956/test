#! /usr/bin/using_reactor.py  
# Filename:using_reactor.py  
from twisted.internet import reactor
import time


def printTime():
    print 'Current time is', time.strftime("%H:%M:%S")


def stopReactor():
    print "Stopping reactor",time.strftime("%H:%M:%S")
    reactor.stop()


reactor.callLater(1, printTime)
reactor.callLater(2, printTime)
reactor.callLater(3, printTime)
reactor.callLater(4, printTime)
reactor.callLater(5, stopReactor)

print 'Running the reactor ...',time.strftime("%H:%M:%S")
reactor.run()
print 'Reactor stopped.' 
import time

def hello():
    print("Hello world!===>" + str(int(time.time())))

from twisted.internet import reactor
reactor.callWhenRunning(hello)
reactor.callLater(3, hello)
reactor.run()
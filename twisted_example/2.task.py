import time

def hello(name):
    print("Hello world!===>" + name + '===>' + str(int(time.time())))

from twisted.internet import reactor, task

#循环任务
task1 = task.LoopingCall(hello, 'ding')
task1.start(5)

reactor.callWhenRunning(hello, 'yudahai')
reactor.callLater(2, hello, 'yuyue')

reactor.run()
# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/2'
__content__ = ''
"""

# 必须的模块
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS


# 继承WebSocketServerProtocol类
class MyServerProtocol(WebSocketServerProtocol):
    # 建立websocket时调用的函数
    def onOpen(self):
        print "open"
        # websocket关闭时调用的函数，其中wasClean指示是否正常关闭，code指示关闭状态，reason指示原因

    def onClose(self, wasClean, code, reason):
        print "close"
        # 收到消息后的处理函数，其中binary指示是字符串形式还是二进制

    def onMessage(self, msg, binary):
        print msg
        # 发送消息，binary意义同上
        self.sendMessage(msg, binary)
        # 发送消息，默认字符串形式
        self.sendMessage(msg)

def start():
    websocket_factory = WebSocketServerFactory()
    websocket_factory.protocol = MyServerProtocol
    websocket_factory.port = 9000
    listenWS(websocket_factory)

if __name__ == '__main__':
    start()
    reactor.run()

if __name__ == '__main__':
    start()
    reactor.run()
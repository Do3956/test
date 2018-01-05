# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/2'
__content__ = ''
"""

from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketClientProtocol, WebSocketClientFactory, connectWS


class MyClientProtocol(WebSocketClientProtocol):
    # 连接建立时调用的函数  
    def onOpen(self):
        # 发送消息  
        self.sendMessage("Hello, world!")
        # 收到消息后的处理函数，参数意义同上

    def onMessage(self, msg, binary):
        print "Got: " + msg


if __name__ == '__main__':
    websocket_factory = WebSocketClientFactory()
    websocket_factory.protocol = MyClientProtocol
    websocket_factory.port = 9000
    connectWS(websocket_factory)

    # factory = WebSocketClientFactory("ws://localhost:9000")
    # factory.protocol = MyClientProtocol
    # connectWS(factory)
    reactor.run()
# -*- coding: utf-8 -*-
'''
异步写入rabbitmq，TornadoConnection本身已经是异步模式
callback模式适用于需要对数据写入后进行处理的情况
但是此模式会拖慢执行速度

@tornado.web.asynchronous模式下，用户
'''
import platform
import os
import sys
import time
import datetime
import logging as logger
import pika
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from pika.adapters.tornado_connection import TornadoConnection



class Fib(tornado.web.RequestHandler):
    """Uses an aysnchronous call to an RPC server to calculate fib(x).

    As with examples of asynchronous HTTP calls, this request will not finish
    until the remote response is received."""

    @tornado.web.asynchronous
    def get(self):
        # print 1111111111111
        self.ts = time.time()
        msg = 'this is a test'
        self.msg = msg
        self.mq_ch = pika_client.channel
        self.queue_name = "queue_name"
        print 55555555,datetime.datetime.now().microsecond
        # Trying to bind to the nameless exchange breaks the program.
        #9.57099986076
        for i in xrange(100):
            self.mq_ch.queue_declare(queue=self.queue_name, callback=self.on_queue_bind)
        self.write('11111')
        print 666666666666666,datetime.datetime.now().microsecond
        self.flush()#支持异步的关键
        # return


    def on_queue_bind(self, frame):
        # print 'on_queue_bind',datetime.datetime.now().microsecond
        # time.sleep(1)
        self.mq_ch.basic_publish(exchange='', routing_key=self.queue_name,
                                 body=str(self.msg))
        # print 'on_queue_bind...end',datetime.datetime.now().microsecond
        # print time.time() -self.ts
        # self.finish()


class PikaClient(object):
    """A modified class as described in pika's demo_tornado.py.
    It handles the connection for the Tornado instance. Messaging/RPC
    callbacks are handled by the Tornado RequestHandler above."""

    def __init__(self):
        self.connecting = False
        self.connection = None
        self.channel = None

    def connect(self):
        # print 22222222
        if self.connecting:
            logger.info('Already connecting to RabbitMQ.')
            return
        logger.info("Connecting to RabbitMQ")
        self.connecting = True
        creds = pika.PlainCredentials('zyl', 'pwd_zyl')
        params = pika.ConnectionParameters(host='112.74.75.38', port=5672,
                                     credentials=creds)
        self.connection = TornadoConnection(params,
                                            on_open_callback=self.on_connect)
        self.connection.add_on_close_callback(self.on_closed)
        # print 4444444444

    def on_connect(self, connection):
        self.connection = connection
        connection.channel(self.on_channel_open)

    def on_channel_open(self, channel):
        logger.info('Channel Open')
        self.channel = channel

    def on_exchange_declare(self, frame):
        logger.info("Exchange declared.")

    def on_basic_cancel(self, frame):
        logger.info('Basic Cancel Ok.')
        # If we don't have any more consumer processes running close
        self.connection.close()

    def on_closed(self, connection):
        # We've closed our pika connection so stop the demo
        print 'close'


pika_client = PikaClient()
pika_client.connect()

def main():
    port = 8003
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", Fib)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()



if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/10/24'
__content__ = ''
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado import gen
import time
from tornado.httpclient import AsyncHTTPClient
import tornado.web

from tornado.options import define, options
define("port", default=8002, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous #保持连接，不主动断开
    def get(self):
        # greeting = self.get_argument('greeting', 'Hello')
        # self.write(greeting + ', friendly user!')
        # return
        print 22222,time.time()
        client = AsyncHTTPClient()
        rst = client.fetch("http://www.facebook.com", request_timeout=3, callback=self.test_callback)
        print rst
        self.flush()

    def test_callback(self, response):
        print response
        print response.error
        print response.body
        # self.write(response.body)
        self.write('11111')
        '''
        refer the offical document, we are responsible for the invocation of the finish function in the async case.
        '''
        self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
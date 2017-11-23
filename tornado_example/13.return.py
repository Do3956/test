# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/10/24'
__content__ = '异步返回值'
"""
import time
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
import tornado.web

from tornado.options import define, options
define("port", default=8003, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        url = 'https://api.github.com/'
        url = 'http://www.facebook.com'
        print time.time(),url
        http_client = AsyncHTTPClient()
        response = yield tornado.gen.Task(http_client.fetch, url)
        print time.time(), response.code
        print response.body
        self.write('13656')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
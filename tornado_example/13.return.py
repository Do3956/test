# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/10/24'
__content__ = '异步返回值'
"""
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen
import sys

import urllib
import json
import datetime
import time
import traceback

from tornado.options import define, options
define("port", default=8003, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    f = sys._getframe()
    filename = f.f_back.f_code.co_filename
    lineno = f.f_back.f_lineno
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        f = sys._getframe()
        filename = f.f_back.f_code.co_filename
        lineno = f.f_back.f_lineno
        print 'call by:',filename,lineno
        print 111111,time.time()
        # url = 'http://www.google.com'
        url = self.get_argument('url', 'www.google.com')
        url = 'http://' + url
        print 'url', url
        client = tornado.httpclient.AsyncHTTPClient()
        print 'here'
        response = yield tornado.gen.Task(client.fetch, url, request_timeout=5)
        # response = 'hhhhh'
        print 222222,time.time()
        print response
        self.write("123")
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
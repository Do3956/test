# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/17'
__content__ = ''
"""

import urllib
import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class getUrlPost(tornado.web.RequestHandler):
    def post(self,number):
        print type(number), number, number.isdigit()
        number = str(number)
        print type(number), number, isinstance(number, int), number.isdigit()

class getUrl(tornado.web.RequestHandler):
    def get(self,number):
        print type(number), number, number.isdigit()
        number = str(number)
        print type(number), number, isinstance(number, int), number.isdigit()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/([0-9]*)", getUrl),
            (r"/getUrlPost/(\w*)", getUrlPost),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
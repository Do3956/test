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


class ReverseHandler(tornado.web.RequestHandler):
    # http://localhost:8000/reverse/?a=23&b=1
    def get(self):
        print self.get_argument('a')
        print self.get_argument('b')
        self.write("1232")


class getUrl(tornado.web.RequestHandler):
    def get(self):
        info = {'a':'login_check', 'b':'17603092933'}
        params = urllib.urlencode(info)
        client = AsyncHTTPClient()
        # url = "http://localhost:8000/reverse/?a=23&b=1"
        url = "http://localhost:8000/reverse/?"
        rst = client.fetch(url, method='GET', request_timeout=3, body=params)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/reverse/", ReverseHandler),
            (r"/", getUrl)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
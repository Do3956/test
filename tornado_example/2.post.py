# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/17'
__content__ = ''
"""

import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        print 111111111
        print self.request.body
        print self.get_argument('text')
        print 2222222222
        text = self.get_argument('text')
        self.add_header("Access-Control-Allow-Origin", "*")
        self.write(textwrap.fill(text))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/", WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
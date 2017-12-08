# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/17'
__content__ = ''
"""

import urllib
import textwrap
import ujson
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)


class getUrl(tornado.web.RequestHandler):
    def get(self):
        client = AsyncHTTPClient()
        url = "http://120.24.36.18:23457/phone"
        data = {"key": "login_check", "phone": "17603092933", "code": "1234", "action": 'test'}

        rst = client.fetch(url, method='POST', request_timeout=3, callback=self.handle_response, body=ujson.dumps(data))

    def handle_response(self, response):
        if response.error:
            print("Error: %s" % response.error)
        else:
            print(response.body)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", getUrl),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
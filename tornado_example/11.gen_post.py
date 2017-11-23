# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/10/24'
__content__ = ''
"""
import json,time
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado import gen
from tornado.httpclient import AsyncHTTPClient
import tornado.web

from tornado.options import define, options
define("port", default=8002, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    # @tornado.web.asynchronous
    def get(self):
        print 22222,time.time()
        url = 'http://120.76.98.236:23457/phone'
        url = 'http://www.google.com'

        info = json.dumps({'key':'login_check', 'phone':'17603092933', 'code':'6666', 'action':'test'})
        client = AsyncHTTPClient()
        rst = client.fetch(url, method='POST', request_timeout=3, callback=self.handle_response, body=info)
        print rst
        # self.flush()#支持异步的关键

    def handle_response(self, response):
        if response.error:
            print time.time(), ("Error: %s" % response.error)
            # self.write(json.dumps(response.body))#此处会报错
        else:
            self.write(json.dumps(response.body))
            print(response.body)

        # self.finish()#支持异步的关键

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
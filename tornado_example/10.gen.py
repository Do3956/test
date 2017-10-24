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
from tornado.httpclient import AsyncHTTPClient
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        # greeting = self.get_argument('greeting', 'Hello')
        # self.write(greeting + ', friendly user!')
        # return
        print 22222
        client = AsyncHTTPClient()
        rst = client.fetch("http://www.facebook.com", request_timeout=2, callback=self.test_callback)
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

# @gen.coroutine
# def GetUser():
#     client = AsyncHTTPClient()
#
#     resp = yield client.fetch("https://api.github.com/users")
#     print 11111, resp.body
#     if resp.code == 200:
#         print resp.body
#     else:
#         resp = {"message": "fetch client error"}
#     print("client fetch error %d, %s" % (resp.code, resp.message))
#     raise gen.Return(resp)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
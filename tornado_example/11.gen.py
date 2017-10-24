# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/10/24'
__content__ = ''
"""

import logging

import tornado.httpserver
import tornado.ioloop
import tornado.web

from tornado.httpclient import AsyncHTTPClient


class MainHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        http.fetch("http://localhost:8084/async-sync-test/", callback=self._test_callback)
        self.write("Hello to the Tornado world! ")
        '''
        Flushes the current output buffer to the network.
        '''
        self.flush()

    '''
    _test_callback is a callback function used for the processing of the response from the async request
    '''

    def _test_callback(self, response):
        print response,type(response)
        print response.body,type(response.body)
        # self.write(response.body)
        self.write(u'43242')
        '''
        refer the offical document, we are responsible for the invocation of the finish function in the async case.
        '''
        self.finish()


settings = {
    # "debug": True,
}

application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8083)
    tornado.ioloop.IOLoop.instance().start()
# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/12'
__content__ = 'tornado自带的AsyncHTTPClient模块，1秒9000-9500
'
"""
import time
import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
def handle_request(response):
    return

url = 'http://www.baidu.com'
# url = 'http://127.0.0.1:8001'
num = 9500
i = 1

start = time.time()
while i<num:
    i += 1
    req = tornado.httpclient.HTTPRequest(url)
    http_client = AsyncHTTPClient()
    http_client.fetch(req, handle_request)
print 'use:', time.time()-start

tornado.ioloop.IOLoop.instance().start()

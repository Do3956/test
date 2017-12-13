# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/12'
__content__ = ''
"""

import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
def handle_request(response):
    if response.error:
        print ("Error:", response.error)
    else:
        print(response.body)
param = {"msg":"111"}
param["img_msg"] = open("t.jpg",'r',encoding='utf-8')
url = 'http://gc.ditu.aliyun.com/geocoding?a=苏州市'
i = 1
print(param)
req = tornado.httpclient.HTTPRequest(url, 'POST', body=str(param))
http_client = AsyncHTTPClient()
while i<10000:
    i += 1
    http_client.fetch(req, handle_request)
tornado.ioloop.IOLoop.instance().start()

# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/9'
__content__ = ''
"""

# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/17'
__content__ = ''
"""

import textwrap
import ujson

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

import hashlib
import base64
from Crypto.Cipher import AES

AES_KEY = 'f9Ol@I6^v7r4+&!.'
CIPHER = AES.new(AES_KEY)

BS = AES.block_size
PAD = lambda s: s + (BS-len(s)%BS) * chr(BS-len(s)%BS)
UNPAD = lambda s: s[0:-ord(s[-1])]


def encrypt(data):
    data = CIPHER.encrypt(PAD(data))
    data = base64.b64encode(data)
    return data

def decrypt(data):
    data = base64.b64decode(data)
    data = UNPAD(CIPHER.decrypt(data))
    return data

def md5(str):
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        data =  self.request.body
        data = decrypt(data)
        data = ujson.loads(data)
        print type(data), data



        nickname = data.get('nickname')
        sign = data.get('sign')

        print 'sign', sign

        del data['sign']

        sort_data = sorted(data.iteritems(), key=lambda a: a[0])
        real_sign = ujson.dumps(sort_data, ensure_ascii=False)

        print 'sort_data', sort_data
        print 'sort_data', str(sort_data),md5(str(sort_data))
        print 'real_sign', md5(real_sign)


        print type(nickname), nickname, md5('你好'), md5(ujson.dumps(nickname))
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write("111")


if __name__ == "__main__":
    # tornado.options.parse_command_line()
    # app = tornado.web.Application(
    #     handlers=[
    #         (r"/old/", WrapHandler)
    #     ]
    # )
    # http_server = tornado.httpserver.HTTPServer(app)
    # http_server.listen(options.port)
    # tornado.ioloop.IOLoop.instance().start()

    b = '912748c37c261a6fc47ce40e41a9a48b'
    data = {'userid': 4575141, 'ts': 1515481917, 'token': '', 'targetKey': 93, 'nickname': '你好'}
    sort_data = sorted(data.iteritems(), key=lambda a: a[0])
    real_sign = ujson.dumps(sort_data, ensure_ascii=False)

    print md5(real_sign)

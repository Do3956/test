# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/11/16'
__content__ = ''
"""

#coding:utf-8

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

import requests
import time
import base64
import ujson

url = 'http://120.25.171.126:30000/getClientVersionInfo/'
url = 'https://web1.ganggui.com.cn:51000/getClientVersionInfo/'

data = {
    "UniqueSerial":'000000-001-157',
    "ts":int(time.time()),
        }

sort_data = sorted(data.iteritems(), key=lambda a:a[0])
sign = ujson.dumps(sort_data, ensure_ascii=False)
data['sign'] = md5(sign)


data = ujson.dumps(data)
data = encrypt(data)

rst = requests.post(url, data=data)
result = rst.content

result = decrypt(result)
print result, type(result)
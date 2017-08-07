# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/4'
__content__ = ''
"""
import base64

def rc4(data,key):
    x = 0
    box = range(256)
    for i in range(256):
        x = (x + box[i] + ord(key[i % len(key)])) % 256
        box[i], box[x] = box[x], box[i]
    x = 0
    y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)


if __name__ == '__main__':
    key = 'hello'
    data = 'hello'
    data = rc4(data,key)
    print data
    print rc4(data,key)
    print base64.b64encode(rc4(data,key))
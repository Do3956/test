# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/4'
__content__ = ''
"""
#coding=utf-8

import sys,os,hashlib,time,base64
class rc4:

  def __init__(self,public_key = None):
    self.public_key = public_key or 'none_public_key'
    self.public_key = hashlib.md5(public_key).hexdigest()
  def encode(self,string):
    self.result = ''
    self.docrypt(string)
    self.result = base64.b32encode(self.result)
    return self.result

  def decode(self,string):
    self.result = ''
    string = base64.b32decode(string)
    self.docrypt(string)
    return self.result

  def docrypt(self,string):
    string_lenth = len(string)
    result = ''
    box = list(range(256))
    randkey = []
    key_lenth = len(self.public_key)

    for i in xrange(255):
      randkey.append(ord(self.public_key[i % key_lenth]))

    for i in xrange(255):
      j = 0
      j = (j + box[i] + randkey[i]) % 256
      tmp = box[i]
      box[i] = box[j]
      box[j] = tmp

    for i in xrange(string_lenth):
      a = j = 0
      a = (a + 1) % 256
      j = (j + box[a]) % 256
      tmp = box[a]
      box[a] = box[j]
      box[j] = tmp
      self.result += chr(ord(string[i]) ^ (box[(box[a] + box[j]) % 256]))

_rc4 = rc4('hello')
temp = _rc4.encode('hello')
print temp
print _rc4.decode(temp)
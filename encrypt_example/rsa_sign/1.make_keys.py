# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/31'
__content__ = ''
"""

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

# 伪随机数生成器
random_generator = Random.new().read
print 1111,random_generator
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
print 1111,rsa

# master的秘钥对的生成
private_pem = rsa.exportKey()
with open('master-private.pem', 'w') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'w') as f:
    f.write(public_pem)

rsa = RSA.generate(1024, random_generator)
print 1111,rsa

# ghost的秘钥对的生成
private_pem = rsa.exportKey()
with open('ghost-private.pem', 'w') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('ghost-public.pem', 'w') as f:
    f.write(public_pem)
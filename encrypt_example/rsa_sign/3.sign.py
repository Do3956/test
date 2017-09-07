# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/31'
__content__ = '签名：发送用自己的私钥加密，接收时用对方的公钥解密'
"""
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


def sign_rsa(message):
    with open('master-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
    return signature
        

def check_sign(message, signature):
    with open('master-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        print is_verify
    return is_verify

if __name__ == "__main__":
    message = '269df.65"中文O(∩_∩)O哈哈~*(##16$s4dfs'

    sign = sign_rsa(message)
    print sign
    end_message = check_sign(message, sign)

    print end_message

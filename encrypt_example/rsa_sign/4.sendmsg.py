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

message = '269df.65"中文O(∩_∩)O哈哈~*(##16$s4dfs'
random_generator = Random.new().read


def sign_rsa(message):
    with open('master-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message)
        sign = signer.sign(digest)
        # signature = base64.b64encode(sign)

    with open('ghost-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = cipher.encrypt(message)

    print cipher_text,sign
    return cipher_text,sign


def check_sign(encrypt_text, signature):
    with open('ghost-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(encrypt_text, random_generator)
        # text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)

    with open('master-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(text)
        is_verify = verifier.verify(digest, signature)
        # is_verify = verifier.verify(digest, base64.b64decode(signature))

    print text, is_verify
    return text, is_verify

encrypt_text, sign = sign_rsa(message)
end_message, rst = check_sign(encrypt_text, sign)
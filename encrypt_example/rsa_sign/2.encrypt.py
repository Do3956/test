# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/31'
__content__ = '使用公钥加密，私钥解密'
"""
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

message = '269df.65"中文O(∩_∩)O哈哈~*(##16$s4dfs'
random_generator = Random.new().read

def encrypt_by_rsa(message):
    with open('ghost-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = cipher.encrypt(message)
        # print cipher_text
        return cipher_text
        # cipher_text_base64 = base64.b64encode(cipher_text)
        # print cipher_text_base64
        # return cipher_text_base64


def decrypt_by_rsa(encrypt_text):
    with open('ghost-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(encrypt_text, random_generator)
        # text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
    return text

encrypt_text = encrypt_by_rsa(message)
print encrypt_text
end_message = decrypt_by_rsa(encrypt_text)

print end_message

print random_generator
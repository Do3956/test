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


class MsgRSA():
    def __init__(self, isMaster=1):
        self.digest = SHA.new()
        self.random_generator = Random.new().read

        if isMaster == 1:
            my_private_key = 'master-private.pem'
            other_public_key = 'ghost-public.pem'
        else:
            my_private_key = 'ghost-private.pem'
            other_public_key = 'master-public.pem'

        # print my_private_key,other_public_key

        with open(my_private_key) as f:
            private_key_mine = f.read()
            rsakey_mine_private = RSA.importKey(private_key_mine)
            self.signer = Signature_pkcs1_v1_5.new(rsakey_mine_private)
            self.cipher_mine_private = Cipher_pkcs1_v1_5.new(rsakey_mine_private)

        with open(other_public_key) as f:
            public_key_other = f.read()
            rsakey_other_public = RSA.importKey(public_key_other)
            self.cipher_other_public = Cipher_pkcs1_v1_5.new(rsakey_other_public)
            self.verifier = Signature_pkcs1_v1_5.new(rsakey_other_public)

    def create_keys(self):
        # rsa算法生成实例
        rsa = RSA.generate(1024, self.random_generator)

        # master的秘钥对的生成
        private_pem = rsa.exportKey()
        with open('master-private.pem', 'w') as f:
            f.write(private_pem)

        public_pem = rsa.publickey().exportKey()
        with open('master-public.pem', 'w') as f:
            f.write(public_pem)

        # ghost的秘钥对的生成
        rsa = RSA.generate(1024, self.random_generator)
        private_pem = rsa.exportKey()
        with open('ghost-private.pem', 'w') as f:
            f.write(private_pem)

        public_pem = rsa.publickey().exportKey()
        with open('ghost-public.pem', 'w') as f:
            f.write(public_pem)

    def sign_rsa(self, message):
        digest = SHA.new()
        digest.update(message)
        sign = self.signer.sign(digest)
        return sign

    def send_msg(self, message):
        sign = self.sign_rsa(message)
        cipher_text = self.cipher_other_public.encrypt(message)
        return cipher_text, sign

    def revice_msg(self, encrypt_text, signature):
        message = self.cipher_mine_private.decrypt(encrypt_text, self.random_generator)
        is_verify = self.check_sign(message, signature)
        return message, is_verify

    def check_sign(self, message, signature):
        digest = SHA.new()
        digest.update(message)
        is_verify = self.verifier.verify(digest, signature)
        return is_verify


if __name__ == "__main__":
    text = '269df.65"中文O(∩_∩)O哈哈~*(##16$s4dfs'
    msg_rsa = MsgRSA()
    encrypt_text, sign = msg_rsa.send_msg(text)
    # print encrypt_text
    # print sign
    #
    # print '-----------'
    msg_rsa2 = MsgRSA(0)
    end_text, is_verify = msg_rsa2.revice_msg(encrypt_text, sign)
    print end_text
    print is_verify
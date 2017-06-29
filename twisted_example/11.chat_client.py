#coding:utf8
"""
简单用
telnet ip port
即可测试
"""

import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",8123))

# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/8'
__content__ = 'pydoc 为python自带库
python -m pydoc -w use_pydoc'
"""
import base64

def test():
    a = '浮点数'
    b = a.decode(encoding="utf8")
    c = b.encode(encoding="gbk")
    print a,b,c,type(a),type(b),type(c)

    print base64.b64encode(a)
    # print base64.b64encode(b)
    print base64.b64encode(c)



class a():
    def __init__(self):
        pass

test()
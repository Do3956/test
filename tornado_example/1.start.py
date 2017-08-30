# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/8/15'
__content__ = '可以指定端口'

"""

import os

port = 7555
cmd = "python 1.hello.py --port=%s" % port
os.system(cmd)

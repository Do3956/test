# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/12'
__content__ = 'requests同步测试，每秒35个左右'
"""

import requests
import time

url = 'http://www.baidu.com'
# url = 'http://127.0.0.1:8001'
num = 10
i = 1

start = time.time()
while i<num:
    i += 1
    requests.get(url)

useTs = time.time()-start
print 'use:', useTs, num/useTs
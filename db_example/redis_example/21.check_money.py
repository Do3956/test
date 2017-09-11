# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/9/11'
__content__ = ''
"""

import redis
from redis import sentinel

host = 'r-t4nc28090602a3b4.redis.singapore.rds.aliyuncs.com'
port = 6379
pwd = 'ZJOaGpoSbtGMD8GajyYbH6l7'

rds = redis.Redis(host=host, port=port, password=pwd)
pip = rds.pipeline(transaction=False)
keys = rds.keys("hu:*")

counter = 0
for k in keys:
    pip.hgetall(k)
rst = pip.execute()

for ret in rst:
    if ret.get('money') < 100:
        print 'not enough money...'
print "over."

# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/4'
__content__ = '监视和 单例 的顺序不一样！
监视：
r.zadd(key,value,name)
单例：
r.zadd(key,name,value)
'
"""

import redis
from redis.sentinel import Sentinel
import time
import ujson

host = [["120.25.174.76", 27380], ["120.25.174.76", 27379]]
password = 'Zyl_Baoshi@redis#1'
sentinel = Sentinel(host)

print sentinel.discover_master('mymaster')

r = sentinel.master_for('mymaster',password=password, redis_class = redis.Redis)

r.pipeline(transaction=False)
# r.zadd('att:all_rank:20180102',700,ujson.dumps({'nickname': u'dtttgh', 'userid': 1439091}))
# r.zadd('att:all_rank:20180102',700,ujson.dumps({'nickname': u'dtttgh', 'userid': 1439091}))
data= ujson.dumps({'nickname': u'dtttgh', 'userid': 1439091})

# r.zadd('att:all_rank:20180102',data=700)
r.zadd('att:all_rank:20180102',data,700)

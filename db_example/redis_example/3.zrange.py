# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/4'
__content__ = '取前20个'
"""

import redis
import time
import ujson

with open("config.json") as f:
    config = ujson.load(f)
host = config.get("host")
port = config.get("port")
pwd = config.get("pwd")

r = redis.Redis(host=host, port=port, password=pwd)


print r.zrevrange("att:all_rank:20180129",0,19,withscores=True)
# print r.zrange("att:all_rank:20180129",-20,-1,withscores=True, desc=True)

#coding:utf8
#批量获取哈希数据

import redis
import time

host = '120.24.36.18'
port = 7379
password = 'Zyl_Baoshi@redis#1'

dbid = 4

r = redis.Redis(host=host, port=port, password=password)

# print '------------普通获取'
# start = time.time()
# print r.hgetall('hu:2248')
# print r.hgetall('hu:2247')
# print 'use:', time.time() - start

# print '------------批量获取'
# start = time.time()
p = r.pipeline(transaction=False)
redis_key = 'hu:2248'
p.hgetall(redis_key)
p.hincrby(redis_key, 'money', 1)#
p.hgetall(redis_key)
p.hincrby(redis_key, 'money', 1)#
print p.execute()
# print 'use:', time.time() - start

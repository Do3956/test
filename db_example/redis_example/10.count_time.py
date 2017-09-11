#coding:utf8
# 测试redis操作时长，单进程

import redis
import time
host = '127.0.0.1'
port = 6379
# host = '120.25.174.76'
# port = 8380
# password = 'Zyl_Baoshi@redis#1'

# r = redis.Redis(host=host, port=port, password=password)
r = redis.Redis(host=host, port=port)
p = r.pipeline(transaction=False)

def update_token(conn, token, user, item=None):
    ts = time.time()
    conn.hset('test:login:', token, user)
    conn.zadd('test:recent:', token, ts)
    if item:
        conn.zadd('test:view:%s'%token, item, ts)
        conn.zremrangebyrank('test:view:%s'%token, 0, -26)

user = {'name':'test_from_book','content':'everyone lies..'}
token = '15499fdsihfihfuw'
start = time.time()
for i in xrange(1, 3000):
    update_token(r, token, user, i)
    # p.execute()
print time.time() - start
#
# #连接池
# print '------------连接池'
# pool = redis.ConnectionPool(host=host, port=port)
# r = redis.Redis(connection_pool=pool)
# r.set('name','do')
# print r.get('name')
#
# #管道，一次执行多个操作
# print '------------管道'
# pool = redis.ConnectionPool(host=host, port=port)
# r = redis.Redis(connection_pool=pool)
# pipe = r.pipeline(transaction=True)
# r.set('name','do')
# r.set('job','e')
# pipe.execute()
#
# print r.get('name')
# print r.get('job')
#

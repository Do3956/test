#coding:utf8
import redis

host = '127.0.0.1'
port = 6379

dbid = 4

#普通连接
print '------------普通连接'
r = redis.Redis(host=host, port=port)
r.set('name','do')
print r.get('name')

#连接池
print '------------连接池'
pool = redis.ConnectionPool(host=host, port=port)
r = redis.Redis(connection_pool=pool)
r.set('name','do')
print r.get('name')

#管道，一次执行多个操作
print '------------管道'
pool = redis.ConnectionPool(host=host, port=port)
r = redis.Redis(connection_pool=pool)
pipe = r.pipeline(transaction=True)
r.set('name','do')
r.set('job','e')
pipe.execute()

print r.get('name')
print r.get('job')


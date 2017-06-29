import txredisapi as redis

redis_store = redis.lazyConnectionPool(dbid=4, host='localhost', port=6379)

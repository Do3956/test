#coding:utf8

#发布，订阅，不建议用，kafka更适合

import redis

class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')
        self.chan_sub = 'fm92.4'
        self.chan_pub = 'fm92.4'

    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_pub)
        pub.parse_response()
        return pub

redisHelper = RedisHelper()
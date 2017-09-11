#coding:utf8

#订阅

from publish_server import redisHelper

while True:
    msg = redisHelper.subscribe().parse_response()
    print msg
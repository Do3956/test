# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/11/6'
__content__ = ''
"""
import pika

print 666666666
credentials = pika.PlainCredentials('zyl','pwd_zyl')
connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials,
    host='112.74.75.38', port=5670, socket_timeout=2, blocked_connection_timeout=2))
print 333333333333
channel = connection.channel()
channel.queue_declare(queue='hello')
for i in xrange(1000):
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World2!')
print 111111111
connection.close()
print 2222222222




# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/11/6'
__content__ = '失败重写机制，断线重连机制'
1.多个进程写？怎么保证不写重复
2.每2秒批量写一次？此模式目前单进程即可，但是否需要主从？
"""

import pika
credentials = pika.PlainCredentials('zyl','pwd_zyl')

connection = pika.BlockingConnection(pika.ConnectionParameters(credentials=credentials,
    host='112.74.75.38', port=5670, socket_timeout=2, blocked_connection_timeout=2))
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)


channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
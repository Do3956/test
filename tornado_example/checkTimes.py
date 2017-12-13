# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/12'
__content__ = ''
"""

#coding:utf-8
#并发为10的情况

import time
import urllib

import gevent
import gevent.monkey

gevent.monkey.patch_all()
i = 0
start = time.time()
count = 1000

def req_url2(url):
    global i
    while True:
        try:
            if i > count:
                print time.time() - start
                break
            i += 1
            s = time.clock()
            c = urllib.urlopen(url)
            # print("req...consume:%s" % (time.clock() - s))
        except Exception as e:
            print("req failed.", e)
        gevent.sleep(0.1)


if __name__ == "__main__":
    # url = 'http://127.0.0.1:8001'
    url = 'http://120.24.36.18:5200/?userid=1'

    tasks = [gevent.spawn(req_url2, url) for i in range(4)]
    gevent.joinall(tasks)
    print("all competed:%s",time.time() - start)


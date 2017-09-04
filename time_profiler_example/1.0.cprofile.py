# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/26 18:39 
""" 
import time

def test():
    for i in xrange(1000):
        i = i ** i
    sleep()
    test1()

def test1():
    sleep()

def sum_slow():
    all = 0
    for i in xrange(5000):
        all += i ** i
    return all

def sleep():
    time.sleep(0.5)


test()

#性能分析
_sys_out = 'python -m cProfile -s cumulative formatStr.py'
#输出到文件
_sys_out = 'python -m cProfile -s cumulative -o my.profile formatStr.py'
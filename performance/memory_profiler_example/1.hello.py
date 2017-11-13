# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/23 23:19
yum install psutil
""" 

import time
from memory_profiler import profile

@profile
def my_func():
    a = []
    for i in xrange(10000):
        b = {'net_1,%s'%i:i}
        a.append(i)
        b = [2] * 10000
    # print a,b
    # del b
    del a
    # print "+++++++++"

if __name__ == '__main__':
    my_func()



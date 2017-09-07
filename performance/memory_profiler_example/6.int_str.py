# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/23 23:39 
""" 

from datetime import datetime
from memory_profiler import profile


@profile
def my_func():
    beg = datetime.now()
    a = {}
    for i in range(1000000):
        a[i] = i
        # a[str(i)] = i
    print "+++++++++"
    del a
    print "+++++++++"
    end = datetime.now()
    print "time:", end - beg

if __name__ == '__main__':
    my_func()
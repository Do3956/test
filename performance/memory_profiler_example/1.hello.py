# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/23 23:19 
""" 

import time
from memory_profiler import profile

@profile
def my_func():
    a = [1] * (10 ** 6)
    # b = [2] * (2 * 10 ** 7)
    # print a,b
    time.sleep(1)
    # del b
    del a
    # print "+++++++++"

if __name__ == '__main__':
    my_func()
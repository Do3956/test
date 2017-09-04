# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/23 23:32 
""" 
import time
from memory_profiler import profile

if '__builtin__' not in dir() or not hasattr(__builtin__, 'profile'):
    def profile(func):
        def inner(*args, **kwargs):
            return func(*args, **kwargs)
        return inner

@profile
def test1():
    n = 10000
    a = [1] * n
    time.sleep(1)
    return a

@profile
def test2():
    n = 100000
    b = [1] * n
    time.sleep(1)
    return b

if __name__ == "__main__":
    test1()
    test2()
    print 'finish'

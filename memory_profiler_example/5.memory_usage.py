# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/23 23:37 
"""


def f(a, n=100):
    import time
    time.sleep(2)
    b = [a] * n
    time.sleep(1)
    return b


from memory_profiler import memory_usage

print memory_usage((f, (2,), {'n': int(1e6)}))
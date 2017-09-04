# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/8/26 19:43

打印函数运行时间
"""

import timeit
from ctypes import cdll


def generate_c(num):
    # Load standard C library
    # libc = cdll.LoadLibrary("libc.so.6") #Linux
    libc = cdll.msvcrt  # Windows
    while num:
        yield libc.rand() % 10
        num -= 1


print(timeit.timeit("sum(generate_c(999))", setup="from __main__ import generate_c", number=1000))
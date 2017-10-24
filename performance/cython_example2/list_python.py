# encoding: utf-8

"""
@version: v1.0
@author: do
@time: 2017/9/19 22:35
"""

def test_list(x,y):
    a = []

    for i in range(10000):
        a.append(x)
        a.append(y)

    return a

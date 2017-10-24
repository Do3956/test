# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/9/12'
__content__ = '帕斯卡三角形'
"""

def getTriangle(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]

    triangle = [1] * n
    for i in range(1, n-1):
        triangle[i] = getTriangle(n-1)[i-1] + getTriangle(n-1)[i]
    return triangle

print(getTriangle(5))
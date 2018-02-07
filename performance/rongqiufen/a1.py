# -*- coding: utf-8 -*-

def mysort(ls):
    # 快排
    if len(ls) == 0:
        return ls
    else:
        return mysort(filter(lambda x: x < ls[0], ls)) + \
               filter(lambda x: x == ls[0], ls) + \
               mysort(filter(lambda x: x > ls[0], ls))


a = [5, 2, 5, 6, 7, 8, 2, 1]
print a
print mysort(a)

print '-------------mysort------------------'
print ''


######################################################################
def mypower(a, x):
    # 快速求幂 a**x
    if x == 0:
        return 1

    t = mypower(a, x / 2)
    if x % 2 == 0:
        return t * t
    else:
        return a * t * t


import time

t = time.clock()
x = 1
for i in xrange(20000):
    x = x * 3
print '%.6f' % (time.clock() - t)

t = time.clock()
x = mypower(3, 20000)
print '%.6f' % (time.clock() - t)

t = time.clock()
x = 3 ** 20000
print '%.6f' % (time.clock() - t)

print '-------------mypower------------------'
print ''


############################## 矩阵快速 斐波那契 ########################################
def mymul(a, b):
    # 矩阵求幂
    return [
        [a[0][0] * b[0][0] + a[0][1] * b[1][0],
         a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0],
         a[1][0] * b[0][1] + a[1][1] * b[1][1]]
    ]


def myf(a, x):
    if x == 1:
        return a

    t = myf(a, x / 2)

    if x % 2 == 0:
        return mymul(t, t)
    else:
        return mymul(a, mymul(t, t))


def fib1(n):
    # 矩阵 斐波那契数列 求法
    mt = [
        [1, 1],
        [1, 0]
    ]
    if n == 0 or n == 1:
        return 1
    rst = myf(mt, n)
    return rst[1][0]


def fib2(n):
    # 普通 斐波那契数列 求法
    a, b, c = 1, 1, 1
    for i in range(2, n):
        c = a + b
        b, a = c, b
    return c


t = time.clock()
x = fib1(1000)
print '%.6f' % (time.clock() - t)
print x

t = time.clock()
x = fib2(1000)
print '%.6f' % (time.clock() - t)
print x

print '-------------fib------------------'
print ''

################################高斯消元######################################


import numpy as np

a = np.array([
    [1, 1],
    [2, 4]])
b = np.array([35, 94])
x = np.linalg.solve(a, b)
print(x)

a = np.array([
    [1, 1, 1],
    [8, 6, 6],
    [0, 2, 1]])
b = np.array([18, 118, 20])
x = np.linalg.solve(a, b)
print(x)

print '-------------numpy------------------'
print ''
######################################################################
import math


# e^x = 1 + 1/1!x + 1/2!x^2 + 1/3!x^3.....
def myexp(x):
    t = 1.0
    s = 1.0
    rst = 1.0
    for i in range(1, 256):
        t, s = t * i, s * x
        rst += s * 1.0 / t
    return rst


# ln(1+x) = x - x^2/2 + x^3/3 - x4/4.....(-1<x<=1)
ln2 = 0.693147180559945


def myln(x):
    y = (x - 1) * 1.0
    t = 1.0 * y
    rst = y
    for i in range(1, 256):
        t = t * y
        rst += t / (i + 1) * (-1) ** (i % 2)
    return rst


# ln(n)=ln(x*2^c)=ln(x)+cln(2)
def myln1(x):
    c = 0
    while abs(x) >= 2:
        x = x / 2.0
        c = c + 1
    return myln(x) + c * ln2


def mylog(a, b):
    return myln1(a) / myln1(b)


# x^y=e^(ln(x)*y)
def mypow(a, b):
    return myexp(myln1(a) * b)


print 'a', myln(0.5), math.log(0.5), myln1(0.5)
print 'b', mylog(3, 6), math.log(3, 6)
print 'c', mypow(3.45, 7.984), math.pow(3.45, 7.984)

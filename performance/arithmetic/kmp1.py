# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/8'
__content__ = ''
"""

def getNext_1(t, next_list):
    next_list[0] = -1
    j = 0
    k = -1
    while j < len(t) - 1:
        if k == -1 or t[j] == t[k]:
            j = j + 1
            k = k + 1
            next_list[j] = k
        else:
            k = next_list[k]
    print next_list


getNext_1([1,2,34,5], [-2 for i in xrange(100)])
getNext_1([1,2,34,1,34,5], [-2 for i in xrange(100)])
getNext_1([2,2,34,1,34,5], [-2 for i in xrange(100)])
getNext_1([1,2,34,2,34,5], [-2 for i in xrange(100)])
getNext_1([1,2,34,1,2,34,5], [-2 for i in xrange(100)])
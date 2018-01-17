# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = '迭代重载'
"""

class indexer:
    # def __getitem__(self, index): #iter override
    #     return index ** 2
    def __getitem__(self, index): #iter override
        return index * 2
X = indexer()
X[2]
for i in range(5):
    print X[i]
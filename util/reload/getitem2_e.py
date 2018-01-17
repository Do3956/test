# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = '索引重载'
"""


class stepper:
    def __getitem__(self, i):
        return self.data[i]


X = stepper()
X.data = 'Spam'
X[1]  # call __getitem__

for item in X:  # call __getitem__
    print item
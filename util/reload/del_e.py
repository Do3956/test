# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = '析构函数重载'
"""


class Life:
    def __init__(self, name='name'):
        print 'Hello', name
        self.name = name

    def __del__(self):
        print 'Goodby', self.name


brain = Life('Brain')  # call __init__
brain = 'loretta'  # call __del__
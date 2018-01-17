# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = ''
"""


class empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError, attrname


X = empty()
print X.age  # call__getattr__


class accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            # Self.attrname = value loops!
            self.__dict__[attr] = value
        else:
            print attr
            raise AttributeError, attr + 'not allowed'


X = accesscontrol()
X.age = 40  # call __setattr__
X.name = 'wang'  # raise exception
# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2018/1/11'
__content__ = ''
"""

class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used
    in addition to `obj['foo']`.

        o = Storage(a=1, b=2, c=3)
        >>> print o
        <Storage {'a': 1, 'c': 3, 'b': 2}>

        >>> o.a = 2
        >>> print o
        <Storage {'a': 2, 'c': 3, 'b': 2}>

        >>> o.d = 4
        >>> print o
        <Storage {'a': 2, 'c': 3, 'b': 2, 'd': 4}>

        >>> del o.b
        >>> print o
        <Storage {'a': 2, 'c': 3, 'd': 4}>

        >>> o.b
        Traceback (most recent call last):
            ...
        AttributeError: 'b'
    """
    def __getattr__(self, key):
        try:
            # print '__getattr__, key',key
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        # print '__setattr__, key', key
        self[key] = value

    def __delattr__(self, key):
        try:
            # print '__delattr__, key', key
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'

o = Storage(a=1, b=2, c=3)
print o
print o.a

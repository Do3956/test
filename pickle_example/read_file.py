# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/27'
__content__ = ''
"""

#使用pickle模块从文件中重构python对象

import pprint, pickle

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
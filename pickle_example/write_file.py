# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/27'
__content__ = ''
"""

#使用pickle模块将数据对象保存到文件

import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

output = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
print selfref_list
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()
# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/4'
__content__ = ''
"""

import requests

url = 'http://120.24.36.18:6686/parameter?userid=432&fds=3f&a=3f'
data = {'userid':123}
rst = requests.post(url, json=data)

print rst.content
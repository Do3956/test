# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/11/16'
__content__ = ''
"""

import requests

rst = requests.post('http://localhost:8000?text=fds', data={})
print rst.content
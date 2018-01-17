# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/12/26'
__content__ = ''
"""

import requests
rst = requests.post("http://127.0.0.1:5000/")
print rst.content
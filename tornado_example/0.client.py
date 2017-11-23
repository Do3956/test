# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/11/16'
__content__ = ''
"""

import requests

print requests.post('http://localhost:8000/getUrlPost/123', data={})
# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/7/20'
__content__ = ''
"""

import re


def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            print('good')
            return 1
    return 0
    print('exit')


validateEmail('lucif323432a@1s39.com')
validateEmail('luci435231423423432423rfsdgdfgea@1s39.com')
validateEmail('luci435231423423432423rfsdgdfgea@1s39.com')
validateEmail('luci435231423423432423rfsdgdfgea@qq.com')
validateEmail('luci435231423423432423rfsdgdfgea@gamil9.com')
validateEmail('la@a.com')
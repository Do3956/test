# -*- coding: utf-8 -*-
"""
__author__ = 'do'
__mtime__ = '2017/9/13'
__content__ = ''
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [Extension("test_1",["test_1.pyx"])]
setup(
    name = "test_1 pyx",
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
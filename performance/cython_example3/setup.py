# encoding: utf-8  

""" 
@version: v1.0 
@author: do 
@time: 2017/9/19 22:52

python setup.py build_ext --inplace
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

setup(
    name='list_cython',
    ext_modules=cythonize([
        Extension("list_cython", ["list_cython.pyx"],
                  include_dirs=[np.get_include()],
                  ),

    ]),
)
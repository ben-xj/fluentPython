from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext_modules = [
    Extension("acceleration.multiply",
              ["acceleration/cython/multiply.pyx"],
              extra_compile_args=['-fopenmp'],
              extra_link_args=['-fopenmp'],
              include_dirs=[np.get_include()]), 
    Extension("acceleration.knapsack",
              ["acceleration/cython/knapsack.pyx"],
              include_dirs=[np.get_include()]), 
    Extension("acceleration.fib",
              ["acceleration/cython/fib.pyx"])
]

setup(
    name='Fluent Python',
    ext_modules=cythonize(ext_modules),
    script_args=["build_ext", "--build-lib", "."]
)

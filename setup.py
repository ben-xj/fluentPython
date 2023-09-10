from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext_modules = [
    Extension("acceleration.multiply",
              ["acceleration/cython/multiply.pyx"],
              include_dirs=[np.get_include()]), 
    Extension("acceleration.knapsack",
              ["acceleration/cython/knapsack.pyx"],
              include_dirs=[np.get_include()])
]

setup(
    name='Fluent Python',
    ext_modules=cythonize(ext_modules),
    script_args=["build_ext", "--build-lib", "."]
)

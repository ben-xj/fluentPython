from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

ext_modules = [
    Extension("func_to_be_cythonized",
              ["func_to_be_cythonized.pyx"],
              include_dirs=[np.get_include()])
]

setup(
    name='Fluent Python',
    ext_modules=cythonize(ext_modules),
    script_args=["build_ext", "--build-lib", "."]
)

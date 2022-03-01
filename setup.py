from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

package = Extension('binomial_pricing_cython', ['binomial_pricing_cython.pyx'], include_dirs=["../base"], extra_compile_args=["-DPLATFORM=linux"])
setup(ext_modules=cythonize([package]))

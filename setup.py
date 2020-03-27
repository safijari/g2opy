import glob
import shutil
from distutils.sysconfig import get_python_lib

from pybind11_cmake import CMakeBuild, CMakeExtension
from setuptools import find_packages, setup
from setuptools.command.install import install

__version__ = "0.0.1"


try:
    import pybind11_cmake
except ImportError:
    print("pybind11-cmake must be installed." "Try \n \t pip install pybind11_cmake")
    import sys

    sys.exit()


setup(
    name="g2opy",
    version=__version__,
    description="Python binding of C++ graph optimization framework g2o.",
    url="https://github.com/uoip/g2opy",
    license="BSD",
    packages=find_packages(),
    ext_modules=[CMakeExtension("g2o")],
    cmdclass=dict(build_ext=CMakeBuild),
    keywords="g2o, SLAM, BA, ICP, optimization, python, binding",
    long_description="""This is a Python binding for c++ library g2o 
        (https://github.com/RainerKuemmerle/g2o).

        g2o is an open-source C++ framework for optimizing graph-based nonlinear 
        error functions. g2o has been designed to be easily extensible to a wide 
        range of problems and a new problem typically can be specified in a few 
        lines of code. The current implementation provides solutions to several 
        variants of SLAM and BA.""",
)

#!/usr/bin/env python

from setuptools import setup
import os
import re
import io

# Read the long description from the readme file
with open("README.rst", "rb") as f:
    long_description = f.read().decode("utf-8")


# Read the version parameters from the __init__.py file. In this way
# we keep the version information in a single place.
def read(*names, **kwargs):
    with io.open(
            os.path.join(os.path.dirname(__file__), *names),
            encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Run setup
setup(name='scc_access',
      packages=['scc_access'],
      version=find_version("scc_access", "__init__.py"),
      description="Package for interacting with EARLINET's Single Calculus Chain through the command line.",
      long_description=long_description,
      url='https://repositories.imaa.cnr.it/public/scc_access/',
      author='Ioannis Binietoglou',
      author_email='ioannis@inoe.ro',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
      ],
      keywords='lidar aerosol SCC',
      install_requires=[
          "requests",
          "pyyaml",
          "netCDF4"
      ],
      entry_points={
          'console_scripts': ['scc_access = scc_access.scc_access:main'],
      },
      )

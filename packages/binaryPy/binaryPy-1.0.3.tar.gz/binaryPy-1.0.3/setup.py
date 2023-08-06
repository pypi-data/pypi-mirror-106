# -*- coding: utf-8 -*-
"""
Created Date: 2021-03-22 Am
@author: XiaoQingLin
@email: xiaoqinglin2018@gmail.com
"""

from os.path import dirname, join
from sys import version_info

import setuptools

if version_info < (3, 0, 0):
    raise SystemExit("binaryPy requires must be python 3.0.0 or later.")

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages()

setuptools.setup(
    name="binaryPy",
    version='1.0.3',
    author="XiaoQingLin",
    license="MIT",
    author_email="xiaoqinglin2018@gmail.com",
    description="binaryPy encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["Cython==0.29.20"],
    entry_points={"console_scripts": ["binaryPy = binaryPy.cmdline:execute"]},
    url="https://github.com/xqlip/binaryPy",
    packages=packages,
    include_package_data=True,
    classifiers=["Programming Language :: Python :: 3"],
)

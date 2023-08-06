# -*- coding:UTF-8 -*-
#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup, find_packages
import sys

setup(
    name="tools_package",
 version="0.1.4",
 author="act",
 author_email="wang.bensen@detvista.com",
 license="Apache License",
 url="https://gitee.com/OTLXM/packages-for-us",
 packages=["tool_package"],
 install_requires=["cx_Oracle <= 7.0.0 ", "traceback2 <= 1.4.0"],
 classifiers=[
        "Environment :: Web Environment",
 "Intended Audience :: Developers",
 "Operating System :: OS Independent",
 "Topic :: Text Processing :: Indexing",
 "Topic :: Utilities",
 "Topic :: Internet",
 "Topic :: Software Development :: Libraries :: Python Modules",
 "Programming Language :: Python",
 "Programming Language :: Python :: 3.8"
 ],
)
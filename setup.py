#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   setup.py
@Time    :   2022/04/08 09:30:12
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu
'''
from setuptools import setup, find_packages

# List of requirements
requirements = []  # This could be retrieved from requirements.txt

# Package (minimal) configuration
setup(
    name="scrapc2db",
    version="1.0.0",
    description="util package for NLO VASP Database",
    packages=find_packages(),  # __init__.py folders search
    install_requires=requirements
)
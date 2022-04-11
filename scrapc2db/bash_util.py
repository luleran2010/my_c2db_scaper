#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   bash_util.py
@Time    :   2022/04/11 12:33:32
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu
'''

import os 
from pathlib import Path
import sys 
import subprocess

# get file base dir
basedir = Path(os.path.dirname(os.path.abspath(__file__)))
topdir  = basedir.joinpath('../')

def build_wgets(): 
    print('\ncompiling wgets')
    # call build script
    bash_script = str(topdir.joinpath('scripts/build-wgets.sh')) 
    run_dir = Path(topdir.joinpath('data/raw/webpage_htmls')) 
    subprocess.call(['sh', bash_script], cwd=run_dir)
    
    # return all the wgets in a list 
    path = topdir.joinpath('data/raw/webpage_htmls/download.sh')
    with open(path, 'r') as fh: 
        lines = fh.readlines() 
    return lines



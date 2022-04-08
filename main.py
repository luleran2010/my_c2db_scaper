#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   main.py
@Time    :   2022/04/08 08:06:59
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu
'''


# %%
import os 
from pathlib import Path
import sys 
import subprocess

# get file base dir
basedir = Path(os.path.dirname(os.path.abspath(__file__)))


def build(): 
    # call build script
    subprocess.call(['sh',str(basedir.joinpath('./scripts/build.sh'))])
    
    # return all the wgets in a list 
    with open('download.sh', 'r') as fh: 
        lines = fh.readlines() 
    return lines

def count_lines(filename):
    with open(filename, 'r') as fh: 
        lines = fh.readlines() 
    return len(lines)



if __name__ == '__main__':
    dir0 = Path(os.getcwd())
    ## build get file
    os.chdir('data/raw/webpage_htmls')
    wgets = build() 
    
    # download files to interim    
    os.chdir(dir0.joinpath('data/interim'))
    
    # download files with wait
    for wget in wgets[:3]: 
        os.system(wget.strip())




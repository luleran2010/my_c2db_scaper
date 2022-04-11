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
from termios import CR2
import os
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
import sys
import time
import random

from sympy import comp

from scrapc2db.bash_util import build_wgets
from scrapc2db.structure import build_structure
from scrapc2db.util import load_json, dump_json
from scrapc2db.data import ScraperC2DB

# get file base dir
basedir = Path(os.path.dirname(os.path.abspath(__file__)))
topdir  = basedir.joinpath('.')

    


if __name__ == '__main__':
    import pandas as pd 

    dir0 = Path(os.getcwd())
    foo = ScraperC2DB(compress_files=False) 
    foo.build() 

    df = pd.DataFrame(foo.all_data).T 
    df.to_csv('c2db_lookup.csv')
    df.to_pickle('c2db_lookup.pkl')

    

    






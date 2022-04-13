#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   build_lookup.py
@Time    :   2022/04/13 09:22:02
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu
'''
#%%
import os 
import sys 
from pathlib import Path
import json
import tarfile 
import shutil 
import pandas as pd 

def load_json(path): 
    with open(path, 'r') as fh: 
        out = json.load(fh)
    return out 

# get file base dir
basedir = Path(os.path.dirname(os.path.abspath(__file__)))
topdir  = basedir.joinpath('../')

# target dir
dumpdir = topdir.joinpath('data/tmp'); dumpdir.mkdir(exist_ok=True)
srcdir  = topdir.joinpath('data/processed')
# get a list of all tar files
tar_files = list(srcdir.glob('*.tar.gz')) 

# loop through tar files
data = dict() 
for tfile in tar_files: 
    print(tfile.name)
    # extract data
    shutil.copy(tfile, dumpdir)
    f = tarfile.open(dumpdir.joinpath(tfile.name)) 
    f.extractall(dumpdir)
    subdir = dumpdir.joinpath(f.getnames()[0])
    data[subdir.name] = load_json(subdir.joinpath('material_data.json'))
    # rm tar and subdir 
    os.system(f'rm {f.name}')
    os.system(f'rm -r {str(subdir)}')
# save to csv
df = pd.DataFrame(data).T
df.to_csv(dumpdir.joinpath('c2db_lookup.csv'))
df.to_pickle(dumpdir.joinpath('c2db_lookup.pkl'))


#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   util.py
@Time    :   2022/04/11 13:43:09
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu
'''

import json 

def load_json(name): 
    with open(name, 'r') as fh: 
        return json.load(fh)

def dump_json(data, name, indent=1): 
    with open(name, 'w') as fh: 
        json.dump(data, fh, indent=indent)
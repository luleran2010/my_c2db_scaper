#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   foo.py
@Time    :   2022/04/08 08:58:26
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu
'''


import json

def load_json(name): 
    with open(name, 'r') as fh: 
        return json.load(fh)
    
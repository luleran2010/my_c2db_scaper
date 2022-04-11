#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   structure.py
@Time    :   2022/04/11 10:46:16
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu


'''

from pymatgen.core import Structure, Lattice, Element, Species
from pymatgen.io.vasp import Poscar
from pymatgen.io.cif import CifWriter
import numpy as np 

import sys; sys.path.append('../')
from scrapc2db.util import load_json

def build_structure(raw_data_json): 
    cell, poscar = None, None
    for fn in [protocol_1, protocol_2]: 
        try: 
            cell, poscar = fn(raw_data_json)
            break
        except: 
            continue
    if cell is None or poscar is None: 
        print('!!! Could not build structure !!! ')
    return cell, poscar 

def protocol_2(raw_data_json): 
    print("\n!!! POSSIBLE ISSUE: Could not build structure via protocol #1, using alternatice protocol !!!")
    rdf = load_json(raw_data_json)
    # get latice
    matrix = rdf['structure.json']['1']['cell']['array']['__ndarray__'][2]
    matrix = np.array(matrix).reshape(3,3)
    lattice = Lattice(matrix)

    # get positions
    coords = rdf['structure.json']['1']['positions']['__ndarray__'][2]
    coords = np.array(coords).reshape(rdf['structure.json']['1']['positions']['__ndarray__'][0])

    # get species
    species = [Element.from_Z(i) for i in rdf['structure.json']['1']['numbers']['__ndarray__'][2] ] 

    # build structure and POSCAR 
    cell = Structure(lattice=lattice,species=species,coords=coords,coords_are_cartesian=True) 
    poscar = Poscar(cell)
    return cell, poscar

def protocol_1(raw_data_json):
    rdf = load_json(raw_data_json)
    # get lattice
    data = rdf['results-asr.relax.json']['kwargs']['data']
    a,b,c = data['a'],data['b'],data['c'] 
    alpha,beta,gamma = data['alpha'],data['beta'],data['gamma'] 
    lattice = Lattice.from_parameters(a,b,c,alpha,beta,gamma)

    # get positions
    data = rdf['results-asr.relax.json']['kwargs']['data']['atoms']['positions']['__ndarray__']
    coords = np.array(data[2]).reshape(data[0])

    # get species
    data = rdf['results-asr.relax.json']['kwargs']['data']
    species  = [Element(i) for i in data['symbols']]

    # build structure and POSCAR 
    cell = Structure(lattice=lattice,species=species,coords=coords,coords_are_cartesian=True) 
    poscar = Poscar(cell)
    return cell, poscar
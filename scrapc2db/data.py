#!/usr/bin/env python3
# -*-coding:utf-8 -*-
'''
@File    :   data.py
@Time    :   2022/04/11 12:31:39
@Author  :   Daniel W 
@Version :   1.0
@Contact :   willhelmd@tamu.edu
'''


# %%
from distutils.command.build import build
import os
import sys
import time
import random
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

from scrapc2db.bash_util import build_wgets
from scrapc2db.structure import build_structure
from scrapc2db.util import load_json, dump_json

class ScraperC2DB (): 
    def __init__(self, get_structures=True, get_material_data=True, compress_files=True, skip_existing=True):
        self.get_structures = get_structures
        self.get_material_data = get_material_data
        self.compress_files = compress_files 
        self.skip_exisiting = skip_existing
        self.dir0 = Path(os.getcwd()) 
        self._mk_data_directories()
        if get_material_data is True: 
            self.all_data = dict() 

    def build(self):
        os.chdir(self.dir0)
        print('\n\n')
        print('-'*10)
        print('Scraping Data')
         
        # build wgets
        wgets = build_wgets()
        print('\n\n')

        # data directories
        self.data_interm = self.dir0.joinpath('data/interim')
        self.data_proces = self.dir0.joinpath('data/processed')
        
        # download c2db database from web
        os.chdir(self.data_interm)
        for n, wget in enumerate(wgets[:]): 
            os.chdir(self.data_interm) 
            rdf = wget.split()[-1]
            
            if self.skip_exisiting is True and Path(rdf).exists() or Path(rdf).joinpath('.gz').exists(): 
                print('\n\tFile exists, skipping this compound')
                continue
            else: 
                os.system(wget.strip())
                
                if self.get_material_data is True: 
                    self.extraxt_mat_data(rdf)
                
                if self.get_structures is True: 
                    self.extraxt_struc_data(rdf)
                
                if self.compress_files is True: 
                    self._compress_files(rdf)

                self._sleep(n)

        # back to top dir
        os.chdir(self.dir0)

    def _compress_files(self,rdf):
        name = Path(rdf).stem 
        print(f'\ncompressing {rdf}, {name}')

        # compress raw data json
        os.chdir(self.data_interm)
        os.system(f'gzip -f {rdf}')

        # compress processed data
        os.chdir(self.data_proces)
        os.system(f'tar -zcvf {name}.tar.gz {name}')
        # remove non-compressed dir
        os.system(f'rm -r {name}')

    def extraxt_struc_data(self, rdf): 
        fname = Path(rdf).stem
        if self.data_interm.joinpath(rdf).exists() is True: 
            # build subdir
            path = self.data_proces.joinpath(fname)
            path.mkdir(exist_ok=True)
            # get structure
            cell, poscar = build_structure(rdf)
            if poscar is not None: 
                poscar.write_file(path.joinpath('POSCAR'))
            
    def extraxt_mat_data(self, rdf):
        fname = Path(rdf).stem
        if self.data_interm.joinpath(rdf).exists() is True:
            # build subdir
            path = self.data_proces.joinpath(fname)
            path.mkdir(exist_ok=True)
            # build mat_data 
            mat_data = self._build_mat_data(rdf)
            # add mat_data to all_data
            self.all_data[fname] = mat_data
            # save json to file
            dump_json(mat_data, path.joinpath('material_data.json'))

    def _build_mat_data(self, raw_data_file): 
        ##  get cell 
        rdf = load_json(raw_data_file)
        
        ## get important data/properties
        mat_data = dict() 
        try: 
            cell, _ = build_structure(raw_data_file)    
            mat_data['formula'] = cell.formula
        except: 
            mat_data['formula'] = rdf['results-asr.structureinfo.json']['kwargs']['data']['formula']
        try: 
            mat_data['cod_id']  = rdf['info.json']['cod_id']
        except: 
            mat_data['cod_id']  = None

        # get structure/symm data
        data = rdf['results-asr.structureinfo.json']['kwargs']['data']
        mat_data['spacegroup'] = data['spacegroup']
        mat_data['spacegroup_num'] = data['spgnum']
        mat_data['pointgroup'] = data['pointgroup']
        mat_data['has_inversion_symmetry'] = data['has_inversion_symmetry']

        # thermo stablitiy
        keys = ['hform','ehull','thermodynamic_stability_level']
        for key in keys: 
            try: 
                data = rdf['results-asr.convex_hull.json']['kwargs']['data']
                mat_data[key] = data[key]
            except:
                mat_data[key] = None

        # get electronic properties
        keys = [ 'gap', 'gap_dir', 'gap_nosoc', 'gap_dir_nosoc', 'cbm', 'cbm_dir', 'vbm', 
                'vbm_dir', 'efermi', 'dipz', 'evac', 'evacdiff', 'workfunction']
        for key in keys: 
            try: 
                mat_data[key] = rdf['results-asr.gs.json']['kwargs']['data'][key]
            except: 
                mat_data[key] = None 

        # get hse properties
        keys = ['gap_dir_hse', 'gap_dir_hse_nosoc', 'gap_hse', 'gap_hse_nosoc', 
                'cbm_hse', 'cbm_hse_nosoc', 'vbm_hse', 'vbm_hse_nosoc','efermi_hse_nosoc', 'efermi_hse_soc',]
        for key in keys: 
            try: 
                mat_data[key] = rdf['results-asr.hse.json']['kwargs']['data'][key]
            except:
                mat_data[key] = None
        
        # get emass data
        keys = ['emass_cb_dir1', 'emass_cb_dir2', 'emass_cb_dir3', 'emass_vb_dir1', 'emass_vb_dir2', 'emass_vb_dir3']
        for key in keys: 
            try: 
                mat_data[key] = rdf['results-asr.emasses.json']['kwargs']['data'][key]
            except:
                mat_data[key] = None


        # get magnetic properties
        try: 
            mat_data['is_magnetic'] = rdf['results-asr.magstate.json']['kwargs']['data']['is_magnetic']
        except: 
            mat_data['is_magnetic'] = None

        # get bader charges
        try: 
            mat_data['bader_charges'] = rdf['results-asr.bader.json']['kwargs']['data']['bader_charges']['__ndarray__'][2]
        except: 
            mat_data['bader_charges'] = None
        try: 
            mat_data['magmoms']       = rdf['results-asr.magstate.json']['kwargs']['data']['magmoms']['__ndarray__'][2]
        except: 
            mat_data['magmoms'] = None

        return mat_data
    
    def _sleep(self, n): 
        # sleep 
        rand_time = random.randrange(5,10,1) + random.uniform(0,1)
        time.sleep(rand_time)
        if n != 0 and n%15 == 0: 
            print('\tsleeping...')
            time.sleep(30)
        if n !=0 and n%100 == 0: 
            print('\tsleeping...')
            time.sleep(60*5)


    def _mk_data_directories(self): 
        if self.dir0.joinpath('data').exists() is False: 
            self.dir0.joinpath('data').mkdir() 
        if self.dir0.joinpath('data/interim').exists() is False: 
            self.dir0.joinpath('data/interim').mkdir(exist_ok=True)
        if self.dir0.joinpath('data/processed').exists() is False: 
            self.dir0.joinpath('data/processed').mkdir(exist_ok=True)
            



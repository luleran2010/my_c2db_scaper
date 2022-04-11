# my_c2db_scaper
A small repo to automatically scrape the C2DB database - an extensize material database of 2D materials and properties calculated via DFT (https://cmrdb.fysik.dtu.dk/c2db/)  

Please cite the origional source: https://iopscience.iop.org/article/10.1088/2053-1583/ac1059

Features:
* Automatically downloads raw data JSONs and saves to disk.  
* Parses raw data JSONs to build a structure file (POSCAR).  
* Parse raw data JSONs for several important materials properties and saves it as a small JSON file.  
* All files are compressed for efficient storage.  
* Can build a lookup table of the C2DB database.

## Environment
Environment Name: **c2db-scraper**.  
Important Packages: 
>Pymatgen   
>ASE  
>Pandas  

Can be build with the environment.yml file via `conda env create -f environment.yml`

Install the project src code  
`conda activate c2db-scraper`  
`pip install -e .`  

## Useage
run main.py `python main.py`  
or   
use packaged python code 

```bat
from scrapc2db.data import ScraperC2DB
scaper = ScraperC2DB(get_structures=True, get_material_data=True, compress_files=True, skip_existing=True)
scraper.build()
```

## File Organization
*data/interm* contains raw data files (e.g.Be4-09dd42ad034e.json). Are compressed with gzip.  
*data/processed* contains processed data (i.e. POSCAR and material_data.json) is stored in a directory (e.g. Be4-09dd42ad034e/)     

## Structures
All C2DB structures are converted to POSCAR files

## Material Properties
The following materials properties are automatically parsed from the raw data file.  
['formula', 'cod_id', 'spacegroup', 'spacegroup_num', 'pointgroup', 'has_inversion_symmetry', 'hform', 'ehull', 'thermodynamic_stability_level', 'gap', 'gap_dir', 'gap_nosoc', 'gap_dir_nosoc', 'cbm', 'cbm_dir', 'vbm', 'vbm_dir', 'efermi', 'dipz', 'evac', 'evacdiff', 'workfunction', 'gap_dir_hse', 'gap_dir_hse_nosoc', 'gap_hse', 'gap_hse_nosoc', 'cbm_hse', 'cbm_hse_nosoc', 'vbm_hse', 'vbm_hse_nosoc', 'efermi_hse_nosoc', 'efermi_hse_soc', 'emass_cb_dir1', 'emass_cb_dir2', 'emass_cb_dir3', 'emass_vb_dir1', 'emass_vb_dir2', 'emass_vb_dir3', 'is_magnetic', 'bader_charges', 'magmoms']

## ToDo: 
- [x] compress raw data JSON file for LT storage. 
- [x] extract and build structure from raw JSON data. 
- [x] extract important material properties found in the C2DB database. 
>- [x] bandgap energy (GGA, HSE, other) 
>- [x] thermoproperties (heat of formation, thermo stability, e_above_hull) 
>- [ ] optical properties? 

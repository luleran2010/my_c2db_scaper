# my_c2db_scaper
A small repo to scrape the C2DB database and build a structure library. 
Automatically scrapes C2DB database. Structures are created from the raw JSON files. Several important materials properties are also extracted and saved with the structure data. All data entrees are then compressed for longterm storage. 

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

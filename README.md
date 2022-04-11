# my_c2db_scaper
A small repo to scrape the C2DB database and build a structure library. 

## Environment
Environment Name: **c2db-scraper**.  
Important Packages: 
>Pymatgen   
>ASE  
>Pandas  

Can be build with the environment.yml file via `conda env create -f environment.yml`


## ToDo: 
- [ ] compress raw data JSON file for LT storage. 
- [ ] extract and build structure from raw JSON data. 
- [ ] extract important material properties found in the C2DB database. 
>- [ ] bandgap energy (GGA, HSE, other) 
>- [ ] thermoproperties (heat of formation, thermo stability, e_above_hull) 
>- [ ] optical properties? 

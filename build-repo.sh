#!/bin/bash 


## setup repo

## setup Conda environment
env='c2db-scraper'
find_in_conda_env(){
    conda env list | grep "${@}" >/dev/null 2>/dev/null
}

if find_in_conda_env $env; then 
    conda activate $env 
else
    conda env create -f environment.yml
fi 






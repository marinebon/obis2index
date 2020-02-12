#!/bin/bash
set -e
# download OBIS data
Rscript ./obis2index/get_data.R
# filter cols & merge MoFs
python3 ./obis2index/filter_and_merge_mofs.py 'fish length'
# calculate abundances
python3 -m obis2index.indicies.get_species_abundances

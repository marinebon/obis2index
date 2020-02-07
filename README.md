# obis2index
Code for going from OBIS data to a biodiversity health index


1. download OBIS data `Rscript ./obis2index/get_data.R`
2. filter cols & merge MoFs `python3 ./obis2index/filter_and_merge_mofs.py 'fish length'`

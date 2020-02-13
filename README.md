# obis2index
Code for going from OBIS data to a biodiversity health index

Use `calculate_indicators.sh` to calculate all indicators and output updated csv files to `./indicies/`.


# data explore
`Rscript obis2index/explore/top_mofs/1_get_data.R` creates csv file.
`python3 obis2index/explore/top_mofs/top_mofs.py` to visualize csv contents.

# obis2index
Code for going from OBIS data to a biodiversity health index

Use `calculate_indicators.sh` to calculate all indicators and output updated csv files to `./indicies/`.

Scripts for fetching obis data and calculating indicators are in `obis2index/indicies`.
Scripts for exploratory data visualizations are in `obis2index/explore`.
All scripts should be run from the root directory of this project.
Data will get downloaded into the `./data` subdirectory and the final indecies output will be put in `./indicies`.


# data explore
`Rscript obis2index/explore/top_mofs/1_get_data.R` creates csv file.
`python3 obis2index/explore/top_mofs/top_mofs.py` to visualize csv contents.

# obis2index
Code for going from OBIS data to a biodiversity health index

Use `calculate_indicators.sh` to calculate all indicators and output updated csv files to `./indicies/`.

Scripts for fetching obis data and calculating indicators are in `obis2index/indicies`.
Scripts for exploratory data visualizations are in `obis2index/explore`.
All scripts should be run from the root directory of this project.
Data will get downloaded into the `./data` subdirectory and the final indecies output will be put in `./indicies`.


# other data visualizations
```
# see most frequent measurement or facts in mof .csv
python3 -m obis2index.explore.top_column_values data/FKNMS-black_grouper-mof.csv measurementType

# see most frequent values in samplingEffort column
python3 -m obis2index.explore.top_column_values data/FKNMS-everything-ocr.csv samplingEffort

python3 -m obis2index.explore.top_column_values data/FKNMS-everything-ocr.csv year
```

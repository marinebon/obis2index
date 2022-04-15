# obis2index
Calculate biodiversity health indicies from DwC Archive data (pulled from OBIS and|or GBIF).

--------------------------------------------------------------------------

☣️ This repo is being used as a jumping-off point for the BioDiversity Indicator Dev Group at the [2022 NOAA IOOS Code Sprint](https://ioos.github.io/ioos-code-sprint/). For more info please see [the code sprint topic page](https://ioos.github.io/ioos-code-sprint/topics/04-biodiversity-indicator-development/).

📣 If you are new here please jump over to the "Discussions" tab and introduce yourself!

--------------------------------------------------------------------------

## Usage
### easy-access mybinder jupyter notebooks
Use the button below to open example `.ipynb` files in the `/notebooks/` directory:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/marinebon/obis2index/HEAD)

This may take some time to start up but it is a very easy way to get started with this repo.

### Scripted
Use `calculate_indicators.sh` to calculate all indicators and output updated csv files to `./indicies/`.

### technical details
Scripts for fetching obis data and calculating indicators are in `obis2index/indicies`.
Scripts for exploratory data visualizations are in `obis2index/explore`.
All scripts should be run from the root directory of this project.
Data will get downloaded into the `./data` subdirectory and the final indecies output will be put in `./indicies`.

# other data visualizations included
```
# see most frequent measurement or facts in mof .csv
python3 -m obis2index.explore.top_column_values data/FKNMS-black_grouper-mof.csv measurementType

# see most frequent values in samplingEffort column
python3 -m obis2index.explore.top_column_values data/FKNMS-everything-ocr.csv samplingEffort

python3 -m obis2index.explore.top_column_values data/FKNMS-everything-ocr.csv year
```

# additional links

Some output from this project can be found on slides 6 & 7 in [this g presentation](https://docs.google.com/presentation/d/1EBbswmn8SE4Ob9gaI_IoPZ8Pc24wGNTVZDGF3ck_gFo/edit?usp=sharing).
These were generated using the `indicators_from_obis` project on Axiom's ResearchWorkspace.
A link to this project (currently defunct) is [here](https://researchworkspace.com/project/5850658/files).

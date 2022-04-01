#!/bin/bash
# this script is used to re-calculate all indicators and populate the .csv files
set -e
# === abundance
Rscript ./obis2index/indicies/abundance_of_black_grouper/1_get_data.R
python3 -m obis2index.indicies.abundance_of_black_grouper.calculate_indicator

Rscript ./obis2index/indicies/abundance_of_hogfish/1_get_data.R
python3 -m obis2index.indicies.abundance_of_hogfish.calculate_indicator

Rscript ./obis2index/indicies/abundance_of_red_grouper/1_get_data.R
python3 -m obis2index.indicies.abundance_of_red_grouper.calculate_indicator

Rscript ./obis2index/indicies/abundance_of_yellowtail_snapper/1_get_data.R
python3 -m obis2index.indicies.abundance_of_yellowtail_snapper.calculate_indicator

# === richness
Rscript ./obis2index/indicies/coral_species_richness/1_get_data.R
python3 -m obis2index.indicies.coral_species_richness.calculate_indicator

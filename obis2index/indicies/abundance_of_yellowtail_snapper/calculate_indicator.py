
from obis2index.util.get_species_abundance import get_species_abundance
from obis2index.util.filter_and_merge_mofs import filter_and_merge_mofs

FILEPATH_ID = 'yellowtail_snapper'
MOF_COL = 'fish length'
filter_and_merge_mofs(FILEPATH_ID, MOF_COL)
get_species_abundance(FILEPATH_ID, MOF_COL, species_name='Ocyurus chrysurus')

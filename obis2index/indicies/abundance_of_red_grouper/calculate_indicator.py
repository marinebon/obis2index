
from obis2index.util.get_species_abundance import get_species_abundance
from obis2index.util.filter_and_merge_mofs import filter_and_merge_mofs

FILEPATH_ID = 'red_grouper'
filter_and_merge_mofs(FILEPATH_ID, 'fish length')


# red grouper
get_species_abundance(species_name='Epinephelus morio')

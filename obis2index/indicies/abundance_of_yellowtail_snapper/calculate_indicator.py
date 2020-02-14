
from obis2index.util.get_species_abundance import get_species_abundance
from obis2index.util.filter_and_merge_mofs import filter_and_merge_mofs

FILEPATH_ID = 'yellowtail_snapper'
filter_and_merge_mofs(FILEPATH_ID, 'fish length')



# yellowtail snapper
get_species_abundance(species_name='Ocyurus chrysurus')

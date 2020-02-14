
from obis2index.util.get_species_abundance import get_species_abundance
from obis2index.util.filter_and_merge_mofs import filter_and_merge_mofs

FILEPATH_ID = 'hogfish'
filter_and_merge_mofs(FILEPATH_ID, 'fish length')
# hogfish
get_species_abundance(species_name='Lachnolaimus maximus')

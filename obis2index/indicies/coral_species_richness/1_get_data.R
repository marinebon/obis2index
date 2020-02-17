source('obis2index/util/fetch_data.R')

# === variables

fetch_data_multispecies(
    'corals',
    scientific_name = c(
        # NOTE: for this to be a true richness calculation this is assumed
        #   to be an exhaustive list of all coral species in FKNMS.
        #   However, this list is not at all close to exhaustive.
        # hard bottom species
        'Siderastrea radians',
        'Porites astreoides',
        'Favia fragum',
        'Diploria strigosa',
        'Dichocoenia stokesii',
        # patch reef species
        'Montastraea annularis',
        'Siderastrea siderea'
        'Acropora palmata',
        # bank reef species
        # Elkhorn, star, and brain corals (already included)
    )
)

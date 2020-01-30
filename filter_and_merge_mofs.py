import pandas as pd


# === variables
obis_records_file = 'data/FKNMS.csv'
obis_mofs_file = 'data/FKNMS_mofs.csv'
obis_records_and_mofs_file = 'data/FKNMS_merged.csv'
measurement_type = 'fish length'  # the only measurement we care about

# === load
print('loading dataframes...')
obis_data = pd.read_csv(obis_records_file, low_memory=False)
obis_mofs = pd.read_csv(obis_mofs_file, low_memory=False)

# === drop all cols except the few we want to keep
print('dropping some columns...')
obis_data = obis_data[[
    'occurrenceID', 'date_year', 'habitat', 'scientificName', 'aphiaID',
    'decimalLatitude', 'decimalLongitude', 'occurrenceStatus',
    'basisOfRecord', 'date_start', 'date_mid', 'date_end',
    'samplingProtocol',
    'maximumDepthInMeters', 'minimumDepthInMeters', 'dataset_id',
    'eventDate', 'datasetName',
    'ownerInstitutionCode', 'samplingEffort', 'depth'
]]
obis_mofs = obis_mofs[[
    'measurementValue', 'occurrenceID', 'measurementType'
]]


# === filter everything except fish_length
print('keeping only "{}" MoFs'.format(measurement_type))
obis_mofs = obis_mofs[obis_mofs['measurementType'] == measurement_type]
# rename measurementValue column to fish_length
obis_mofs = obis_mofs.rename(columns={'measurementValue': 'fish_length'})
obis_mofs = obis_mofs.drop(['measurementValue', 'measurementType'])

# === join the MoF & occurrence dataframes
print("joining dataframes...")
obis_data = obis_data.set_index('occurrenceID')
obis_data_merged = obis_mofs.join(
    obis_data, on="occurrenceID", rsuffix="_occur"
)

# === save
print("saving output...")
obis_data_merged.to_csv(obis_records_and_mofs_file)
print("done")

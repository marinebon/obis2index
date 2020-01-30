import pandas as pd


# === variables
obis_records_file = 'data/FKNMS.csv'
obis_mofs_file = 'data/FKNMS_mofs.csv'
obis_records_and_mofs_file = 'data/FKNMS_merged.csv'

# === load
obis_data = pd.read_csv(obis_records_file, low_memory=False)
obis_mofs = pd.read_csv(obis_mofs_file, low_memory=False)

# === drop all cols except the few we want to keep
obis_data = obis_data[[
    'occurrenceID', 'date_year', 'habitat', 'scientificName', 'aphiaID',
    'decimalLatitude', 'decimalLongitude', 'occurrenceStatus',
    'basisOfRecord', 'date_start', 'date_mid', 'date_end',
    'samplingProtocol', 'recordedBy',
    'maximumDepthInMeters', 'minimumDepthInMeters', 'dataset_id',
    'eventDate', 'datasetName', 'coordinateUncertaintyInMeters',
    'ownerInstitutionCode', 'samplingEffort', 'depth', 'individualCount'
]]
obis_mofs = obis_mofs[[
    'measurementValue', 'occurrenceID', 'measurementType'
]]


# === filter everything except fish_length
obis_mofs = obis_mofs[obis_mofs['measurementType'] == 'fish length']


# === join the MoF & occurrence dataframes
if obis_data.index.name != 'id':
    # prevents None of ['id'] are in the columns when re-running
    obis_data = obis_data.set_index('id')
obis_data_merged = obis_mofs.join(
    obis_data, on="occurrenceID", rsuffix="_occur"
)

# === save
obis_data_merged.to_csv(obis_records_and_mofs_file)

import pandas as pd


def main(measurement_type):
    """
        Merges MoF & occurrence dataframes & filters out all MoF columns except
        the column measurement_type.

        params:
        -----------
        measurement_type : str
            the only measurement we care about
            eg: 'fish length'
    """
    # === variables
    obis_records_file = 'data/FKNMS.csv'
    obis_mofs_file = 'data/FKNMS_fish_len_mofs.csv'
    obis_records_and_mofs_file = 'data/FKNMS_merged_{}.csv'.format(
        measurement_type
    )

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

    # === filter everything except 'measurement_type'
    print('keeping only "{}" MoFs'.format(measurement_type))
    obis_mofs = obis_mofs[obis_mofs['measurementType'] == measurement_type]
    # rename measurementValue column to fish_length
    obis_mofs = obis_mofs.rename(
        columns={'measurementValue': measurement_type}
    )
    obis_mofs = obis_mofs.drop(columns='measurementType')

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
    return obis_data_merged


if __name__ == "__main__":
    main("fish_length")

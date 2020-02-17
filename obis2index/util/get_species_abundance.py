import pandas as pd
from obis2index.util.insert_csv_header import insert_csv_header


def get_species_abundance(
    filepath_id,
    mof_col,
    species_name
):
    """
    Calculates abundance as count per sampling day.
    The assumption here is that only one sample was taken per day.
    Is this a good assumption? Probably not.
    """
    data_file_path = "data/FKNMS-{}-mrg-{}.csv".format(filepath_id, mof_col)
    filtered_df = pd.read_csv(data_file_path, low_memory=False)
    x = []
    y = []
    years = filtered_df.date_year.unique()
    years.sort()

    for year in years:
        x.append(year)

        # subset to just this year
        df_subset = filtered_df[filtered_df['date_year'] == year]
        # assumes one sample per day:
        n_samples = len(df_subset.eventDate.unique())
        # count of 'present'
        count = df_subset[
            df_subset["occurrenceStatus"] == 'present'
        ]['occurrenceStatus'].count()
        abundance = count / n_samples
        y.append(abundance)

    output_df = insert_csv_header(
        pd.DataFrame({
            "year": x,
            "abundance": y
        }),
        header=[
            {"year": "units", "abundance": "count / sampling-day"},
            {"year": "extent", "abundance": "FKNMS"},
        ]
    )
    output_df.to_csv("indicies/abundance_{}.csv".format(
        species_name.replace(' ', '_')
    ))

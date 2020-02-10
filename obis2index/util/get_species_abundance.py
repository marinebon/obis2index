import pandas as pd

# === variables
OBIS_RECORDS_AND_MOFS_FILE = 'data/FKNMS_merged.csv'


def get_species_abundance(species_name='Lachnolaimus maximus'):
    obis_data = pd.read_csv(OBIS_RECORDS_AND_MOFS_FILE, low_memory=False)
    filtered_df = obis_data[obis_data['scientificName'] == species_name]
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

    # plt.plot(x, y)
    # plt.show()

    output_df = pd.DataFrame({
        "time": x,
        "count": y
    })

    output_df.to_csv("indicies/abundance_{}.csv".format(
        species_name.replace(' ', '_')
    ))

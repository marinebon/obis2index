import pandas as pd


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

    # plt.plot(x, y)
    # plt.show()

    # === std csv formatting from
    # https://github.com/mandykarnauskas/GoM-Ecosystem-Status-Report/blob/master/plotIndicatorTimeSeries.r
    #   Column 1 is time values, columns 2+ are indicator data
    #   Time can be in yearly or monthly time steps, MUST be in this format:
    #      YYYY (e.g., 2011) or mmmYYYY (e.g., Jan1986)
    output_df = pd.DataFrame({
        "year": x,
        "abundance": y
    })
    header = [
        #   Row 1 is indicator name (main title of plot)
        #       (Row 1 header element will be injected by to_csv)
        #   Row 2 is units (y-axis label)
        {"year": "units", "abundance": "count / sampling-day"},
        #   Row 3 is spatial extent or other specifying information
        #    ...?
        {"year": "extent", "abundance": "FKNMS"},
    ]
    output_df = pd.concat([pd.DataFrame(header), output_df], ignore_index=True)

    output_df.set_index('year', inplace=True)
    output_df.to_csv("indicies/abundance_{}.csv".format(
        species_name.replace(' ', '_')
    ))

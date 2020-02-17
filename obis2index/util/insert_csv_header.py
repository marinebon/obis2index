import pandas as pd


def insert_csv_header(df, header_rows):
    """
    Insert the std csv formatting header from
    # https://github.com/mandykarnauskas/GoM-Ecosystem-Status-Report/blob/master/plotIndicatorTimeSeries.r
    #   Column 1 is time values, columns 2+ are indicator data
    #   Time can be in yearly or monthly time steps, MUST be in this format:
    #      YYYY (e.g., 2011) or mmmYYYY (e.g., Jan1986)

    Example header_rows:
    ----------------------
    header_rows = [
        #   Row 1 is indicator name (main title of plot)
        #       (Row 1 header element will be injected by to_csv)
        #   Row 2 is units (y-axis label)
        {"year": "units", "richness": "species"},
        #   Row 3 is spatial extent or other specifying information
        #    ...?
        {"year": "extent", "richness": "FKNMS"},
    ]
    """
    output_df = pd.concat([pd.DataFrame(header_rows), df], ignore_index=True)
    output_df.set_index('year', inplace=True)

    return output_df

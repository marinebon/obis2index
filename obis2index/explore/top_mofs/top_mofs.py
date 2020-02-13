"""
Shows sorted count of the most common Measurement or Facts.
Use this to see what kind of MoFs your data subset contains.
"""

import pandas as pd

from obis2index.util.plot_most_common_in_column \
    import plot_most_common_in_column


# variables
obis_mofs_file = 'data/top_mofs-FKNMS_mofs.csv'
obis_mofs = pd.read_csv(obis_mofs_file, low_memory=False)
plot_most_common_in_column(df=obis_mofs, column='measurementType', TOP_N=9)

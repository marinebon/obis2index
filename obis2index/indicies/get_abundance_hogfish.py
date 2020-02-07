import pandas as pd
import matplotlib.pyplot as plt

# === variables
OBIS_RECORDS_AND_MOFS_FILE = 'data/FKNMS_merged.csv'
SPECIES = 'Lachnolaimus maximus'

obis_data = pd.read_csv(OBIS_RECORDS_AND_MOFS_FILE, low_memory=False)
filtered_df = obis_data[obis_data['scientificName'] == SPECIES]
x = []
y = []
years = filtered_df.date_year.unique()
years.sort()
for year in years:
    x.append(year)
    y.append(filtered_df[filtered_df['date_year'] == year].count())
plt.plot(x, y)
plt.show()

import pandas as pd
from obis2index.util.insert_csv_header import insert_csv_header

filepath_id = 'everything'
data_file_path = "data/FKNMS-{}-ocr.csv".format(filepath_id)

print("loading data...")
df = pd.read_csv(data_file_path, low_memory=False)
total_rows = len(df)
print("loaded {} rows.".format(total_rows))
print("filtering non-Anthozoa...")
# filter out non-coral species
df = df[df['class'] == 'Anthozoa']
anth_rows = len(df)
print("{}% Anthozoa records.".format(anth_rows/total_rows*100))

print("calculating richness from {} rows...".format(len(df)))
# richness is one row per year
unique_years = df['year'].value_counts()
richness = pd.DataFrame(columns=('year', 'richness'))
richness.set_index('year')
for year in unique_years.index:
    annualized_subset = df[df['year'] == year]
    # count unique values in species column
    count = len(annualized_subset['scientificName'].unique())
    richness = richness.append(
        {'year': int(year), 'richness': count}, ignore_index=True
    )

print('saving indicator .csv...')
header = [
    {"year": "units", "richness": "species"},
    {"year": "extent", "richness": "FKNMS"},
]
richness = insert_csv_header(richness, header)

richness.to_csv("indicies/richness_corals.csv")

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
unique_years = df['year'].value_counts().sort_values()
richness = pd.DataFrame({
    "year": unique_years,
    "richness": [0]*len(unique_years)
})
for year in unique_years:
    annualized_subset = df[df['year'] == year]
    # count unique values in species column
    richness[year] = annualized_subset['scientificName'].value_counts()

print('saving indicator .csv...')
header = [
    {"year": "units", "richness": "species"},
    {"year": "extent", "richness": "FKNMS"},
]
richness = insert_csv_header(richness, header)

richness.to_csv("indicies/richness_corals.csv")

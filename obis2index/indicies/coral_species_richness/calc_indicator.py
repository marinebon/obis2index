import pandas as pd
from obis2index.util.insert_csv_header import insert_csv_header

filepath_id = 'everything'
data_file_path = "data/FKNMS-{}-ocr.csv".format(filepath_id)
df = pd.read_csv(data_file_path, low_memory=False)

# filter out non-coral species
df = df[df['class'] == 'Anthozoa']

# richness is one row per year
unique_years = df['year'].value_counts().sort()
richness = pd.DataFrame({
    "year": unique_years,
    "richness": [None]*unique_years
})
for year in unique_years:
    annualized_subset = df[df['year'] == year]
    # count unique values in species column
    richness[year] = annualized_subset['scientificName'].value_counts()

header = [
    {"year": "units", "richness": "species"},
    {"year": "extent", "richness": "FKNMS"},
]
richness = insert_csv_header(richness, header)

richness.to_csv("indicies/richness_corals.csv")

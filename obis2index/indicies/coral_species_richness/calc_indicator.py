import pandas as pd

filepath_id = 'everything'
data_file_path = "data/FKNMS-{}-ocr.csv".format(filepath_id)
df = pd.read_csv(data_file_path, low_memory=False)

# TODO: filter out non-coral species
# TODO: count unique values in species column

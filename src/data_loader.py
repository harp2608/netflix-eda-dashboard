import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

# Define dataset path
dataset_path = "netflix_titles.csv"

# Download if not already present
if not os.path.exists(dataset_path):
    api = KaggleApi()
    api.authenticate()

    # Replace with actual dataset info
    api.dataset_download_file('shivamb/netflix-shows', file_name='netflix_titles.csv', path='.')
    
    # Unzip the downloaded file
    import zipfile
    with zipfile.ZipFile("netflix_titles.csv.zip", 'r') as zip_ref:
        zip_ref.extractall('.')

# Load the CSV
df = pd.read_csv(dataset_path)
print(df.head())

    

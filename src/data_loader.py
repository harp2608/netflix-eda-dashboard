import kagglehub
import os
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

import pandas as pd

def download_file():
    # Load the file directly from your repo (after adding it to /data/)
    df = pd.read_csv("netflix_titles.csv")
    return df


    

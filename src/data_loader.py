import kagglehub
import os
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

import pandas as pd


   def download_file():
    df = pd.read_csv("data/netflix_titles.csv")
    return df


    

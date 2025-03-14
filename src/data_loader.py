import kagglehub
import os
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

def download_file():
    # Download latest version
    api = KaggleApi()
    api.authenticate()  #using kaggle.json 
    api.dataset_download_files('shivamb/netflix-shows', path='data/', unzip=True)


    
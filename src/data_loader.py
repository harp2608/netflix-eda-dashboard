import kagglehub
import os
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

import pandas as pd

import kagglehub

# Download latest version
path = kagglehub.dataset_download("shivamb/netflix-shows")

print("Path to dataset files:", path)

    

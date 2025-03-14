import pandas as pd
from pathlib import Path

def filter_year(df, year):
    """filter records based on a year"""
    try:
        year = int(year)
    except TypeError as e:
        print(f"Wrong type of the year: {e}.")
    else:   
        df_recent = df[df['release_year']>year]
        return df_recent
    
def filter_genre(df, genre):
    """filter records based on a genre"""
    try:
        df_genre = df[df['genres']==genre]
        return df_genre
    except ValueError as e:
        return e
    

    



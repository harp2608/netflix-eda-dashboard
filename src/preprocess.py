import pandas as pd
from pathlib import Path
from datetime import datetime

def load_data ():
    """loading csv file in DataFrame"""
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root/"data"/"netflix_titles.csv"
    df = pd.read_csv(data_path)   
    print(df.head())
    return df

def remove_record(df, threshold = 0.4):
    """removing records if they miss more then 40% of data"""
    total_shape = df.shape[1]
    df_cleaned = df.dropna(thresh = threshold)
    return df_cleaned

def remove_duplicated(df):
    """removing duplicates from records"""
    df.drop_duplicates(inplace=True)
    return df

def convert_datatype(df):
    """convertation to the correct data type for the further analysis"""

    df['date_added'] = df['date_added'].apply(parse_date)

    df['type'] = df['type'].astype('category')
    df['country'] = df['country'].astype('category')
    df['rating'] = df['rating'].astype('category')

    df['release_year'] = df['release_year'].astype(int)

    df["date_added"] = pd.to_datetime(df["date_added"])

    return df

def parse_date(date_str):
    """try to parse date if exist, otherwise return None"""
    if not isinstance(date_str, str) or not date_str.strip():
        return None
    date_str = date_str.strip()

    formats = [
        "%B %d, %Y",
        "%b %d, %Y",
        "%Y-%m-%d",
        "%m/%d/%Y",
    ]

    for f in formats:
        try:
            return datetime.strptime(date_str, f)
        except ValueError:
            continue
    return None

def explode_genres(df):
    """explode genres"""
    df["genres"] = df["listed_in"].str.split(", ")
    df_exploded = df.explode("genres")
    save_csv(df_exploded)
    return df_exploded

def save_csv(df):
    """Saving preprocessed data to a CSV file"""
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root/"data"/"netflix_titles_filtered.csv"
    df.to_csv(data_path, index=False)

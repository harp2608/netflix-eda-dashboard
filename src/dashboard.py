import streamlit as st
import analysis
import visualization
import pandas as pd

st.set_page_config(page_title="Netflix Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('data/netflix_titles_filtered.csv')
    return df


def app():
    """EDA presentation"""
    st.title("Netflix Data Dashboard 📺 | Harpreet Kaur") 



    df = load_data()

    #filter by year
    year = st.slider("Choose the minimum release year", min_value = df['release_year'].min(), max_value=df['release_year'].max(), value=2020)
    df_year = analysis.filter_year(df, year)

    #filter by genre
    genres_list = df['genres'].unique()
    selected_genre = st.selectbox("Choose a genre", options = genres_list)
    df_genre = analysis.filter_genre(df, selected_genre)

    col1, col2 = st.columns(2)

    with col1:
        #table after year filterring
        st.subheader(f"Films after {year}")
        st.dataframe(df_year)

        #table after genre filterring
        st.subheader(f'Films in the genre {selected_genre}')
        st.dataframe(df_genre)

    with col2:
        # graphics
        st.subheader("General statistics")
        visualization.graph_data(df)
        visualization.plot_rating_by_year(df)
        visualization.plot_top_genres(df)

if __name__ == "__main__":
    app()

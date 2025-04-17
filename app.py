import streamlit as st
import src.data_loader as data_loader
import src.preprocess as preprocess
import src.analysis as analysis
import src.visualization as visualization

# Streamlit App Entry
def main():
    st.title("📺 Netflix EDA Dashboard")

    # Load Data
    data_loader.download_file()
    df = preprocess.load_data()
    df = preprocess.remove_record(df)
    df = preprocess.remove_duplicated(df)
    df = preprocess.convert_datatype(df)
    df = preprocess.explode_genres(df)

    # Sidebar Filters
    year = st.sidebar.selectbox("Select Year", df['release_year'].sort_values().unique())
    genre = st.sidebar.selectbox("Select Genre", df['genres'].explode().dropna().unique())

    # Filtered Data
    df_year = analysis.filter_year(df, year)
    df_genre = analysis.filter_genre(df, genre)

    # Visualizations
    visualization.graph_data(df)
    visualization.plot_rating_by_year(df_year)
    visualization.plot_top_genres(df_genre)

if __name__ == "__main__":
    main()

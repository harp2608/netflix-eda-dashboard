import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def graph_data(df):
    plt.figure(figsize=(10,5))
    sns.histplot(df["release_year"], bins=20, kde=True)
    plt.title("Distribution of films by year")
    st.pyplot(plt.gcf())  # Show graph during the stramlit process
    plt.clf()             # Clean after rendering

def plot_rating_by_year(df):
    releases_per_year = df.groupby('release_year').size()
    plt.figure(figsize=(10,5))
    sns.lineplot(x=releases_per_year.index, y=releases_per_year.values)
    plt.title("Number of releases by year")
    plt.xlabel("Release year")
    plt.ylabel("Number")
    st.pyplot(plt.gcf())  # Show graph during the stramlit process
    plt.clf()             # Clean after rendering

def plot_top_genres(df, top_n=10):
    """Top popular genres"""

    genre_counts = df['genres'].value_counts().head(top_n)

    plt.figure(figsize=(12,6))
    sns.barplot(x=genre_counts.values, y=genre_counts.index)
    plt.title(f"Top-{top_n} genres on Netflix")
    plt.xlabel("Number of releases")
    plt.ylabel("Genres")
    st.pyplot(plt.gcf())  # Show graph during the stramlit process
    plt.clf()             # Clean after rendering

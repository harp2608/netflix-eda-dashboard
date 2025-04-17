import src.data_loader as data_loader
import src.preprocess as preprocess
import src.analysis as analysis
import src.visualization as visualization
import os

def run_dashboard():
    """Run Streamlit Dashboard"""
    os.system('streamlit run src/dashboard.py')

def main():
    data_loader.download_file()

    df = preprocess.load_data()
    df = preprocess.remove_record(df)
    df = preprocess.remove_duplicated(df)
    df = preprocess.convert_datatype(df)
    df = preprocess.explode_genres(df)

    run_dashboard()

    df_year = analysis.filter_year(df, 2020)
    df_genre = analysis.filter_genre(df, 'Crime TV Shows')

    visualization.graph_data(df)
    visualization.plot_rating_by_year(df)
    visualization.plot_top_genres(df)

if __name__ == "__main__":
    main()

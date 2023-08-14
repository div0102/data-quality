import pandas as pd
import streamlit as st


def show_sample_file_data(df:pd.DataFrame) -> pd.DataFrame:
    return df.head(100)

def read_file(uploaded_file):
    return pd.read_csv(uploaded_file,header=0,sep="\t")

def fetch_file_headers(df) -> list:
    return df.columns.values.tolist()

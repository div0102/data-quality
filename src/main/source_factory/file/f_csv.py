import pandas as pd
import streamlit as st


class SourceCSV:
    def __init__(self, file, header, delimeter) -> None:
        self.file = file
        self.header = header
        self.delimeter = delimeter
        

    def show_sample_file_data(self,df: pd.DataFrame) -> pd.DataFrame:
        return df.head(100)

    def read_file(self):
        return pd.read_csv(
            self.file,
            header=self.header,
            sep=self.delimeter,
            skip_blank_lines=True,
            low_memory=True,
            memory_map=True,
        )

    def fetch_file_headers(self,df) -> list:
        return df.columns.values.tolist()

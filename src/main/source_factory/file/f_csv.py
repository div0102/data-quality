import logging

import pandas as pd
import streamlit as st

logger = logging.getLogger(__name__)

class SourceCSV:
    def __init__(self, file, header, delimeter) -> None:
        self.file = file
        self.header = header
        self.delimeter = delimeter
        

    def show_sample_file_data(self,df: pd.DataFrame) -> pd.DataFrame:
        return df.head(100)

    def read_file(self):
        logging.info(f"got header as {self.header}")
        logging.info(f"got delimeter as {self.delimeter}")
        return pd.read_csv(
            self.file,
            # header='infer',#[0 if self.header else 1],
            delimiter=self.delimeter,
            skip_blank_lines=True,
            low_memory=True,
        )

    def fetch_file_headers(self,df) -> list:
        print(df.columns)
        return df.columns.values.tolist()

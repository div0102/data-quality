import logging

import pandas as pd
import streamlit as st
from ui.dqc import list_all_dqc

logger = logging.getLogger(__name__)


class SourceCSV:
    def __init__(self, file, header, delimeter) -> None:
        self.file = file
        self.header = header
        self.delimeter = delimeter

    def show_sample_file_data(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.head(100)

    def read_file(self):
        delimeter = None if self.delimeter == "space" else self.delimeter
        header = 0 if self.header == "Yes" else "infer"
        return pd.read_csv(
            self.file,
            header=header,
            delimiter=delimeter,
            skip_blank_lines=True,
            low_memory=True,
        )

    def fetch_file_headers(self, df) -> list:
        print(df.columns)
        return df.columns.values.tolist()

    def add_dq_checks_for_cols(self, df):
        session_state = st.session_state

        dq_checks = list_all_dqc()
        headers = self.fetch_file_headers(df)
        # session_state.df = df
        session_state.row = pd.Series(index=headers)
        for col in headers:
            # Create a selectbox for the current column and add the selected value to the current row
            index = (
                dq_checks.index(session_state.row[col])
                if session_state.row[col] in dq_checks
                else 0
            )
            session_state.row[col] = st.selectbox(col, dq_checks, key=col, index=index)
        # Add a button to add a new empty row to the dataframe and clear the values of the selectboxes for the current row
        if st.button("Submit Checks"):
            session_state.df = session_state.df.append(
                session_state.row, ignore_index=True
            )
            session_state.row = pd.Series(index=headers)

        # # Display the resulting dataframe
        # st.dataframe(session_state.df)

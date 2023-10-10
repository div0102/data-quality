import pandas as pd
import streamlit as st
from ui.dqc import generate_dqc_config, list_all_dqc

_RECORD_LIMIT = 100


class SourceSnowflake:
    def __init__(self, connection, database_name, schema_name, table_name) -> None:
        self.snow_connection = connection
        self.database_name = database_name
        self.schema_name = schema_name
        self.table_name = table_name

    def get_table_cols(self):
        get_col_sql = f"Select listagg(column_name,',') from information_schema.columns where TABLE_CATALOG = '{self.database_name}' and TABLE_SCHEMA = '{self.schema_name}'\
        and TABLE_NAME = '{self.table_name}'"
        self.snow_connection.cursor().execute(
            f"USE {self.database_name}.{self.schema_name};"
        )
        get_all_columns = self.snow_connection.cursor().execute(get_col_sql).fetchall()

        return get_all_columns

    def add_dq_checks_for_cols(self):
        session_state = st.session_state

        dq_checks = list_all_dqc()
        col_list = self.get_table_cols()[0][0].split(",")
        print(col_list)
        df = pd.DataFrame()
        session_state.df = df
        session_state.row = pd.Series(index=col_list)
        for col in col_list:
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
            session_state.row = pd.Series(index=col_list)

            generate_dqc_config(
                dqc_col_selection=session_state.df.to_dict(orient="records")[0],
                table_name=self.table_name,
                schema_name=self.schema_name,
                database_name=self.database_name,
            )

    def show_sample_table_data(self):
        get_sample_data = f"select * from {self.database_name}.{self.schema_name}.{self.table_name} limit {_RECORD_LIMIT}"

        sample_data = (
            self.snow_connection.cursor().execute(get_sample_data).fetch_pandas_all()
        )
        self.snow_connection.close()
        return sample_data

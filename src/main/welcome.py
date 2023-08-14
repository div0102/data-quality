from io import StringIO

import numpy as np
import pandas as pd
import streamlit as st
from source_factory.file.f_csv import (fetch_file_headers, read_file,
                                       show_sample_file_data)

st.title('Configure your DQ checks here')
st.sidebar.markdown("# DQ availabilty 🎈")
source = st.sidebar.selectbox("Choose your source for DQ",('Local File', 'AWS S3','GCS', 'Database', 'Snowflake', 'BigQuery'))
if source == 'Local File':
    uploaded_file = st.sidebar.file_uploader(label="Upload File", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
     
    if uploaded_file is not None:
        # To read file as bytes:
        # bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)

        # To convert to a string based IO:
        # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # st.write(stringio)

        # To read file as string:
        # string_data = stringio.read()
        # st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = read_file(uploaded_file=uploaded_file)
        

        headers = fetch_file_headers(dataframe)
        print(headers)
        headers= ['Id','Name','Salary']
        for i in headers:
            print(i)
            st.checkbox(i)
        st.write("Sample Data",dataframe)
        # st.write(headers)
        # st.write(fetch_file_headers(dataframe))

        
if source in ['Database','Snowflake','Bigquery']:
    # Add a selectbox to the sidebar:
    database_selectbox = st.sidebar.selectbox(
        'Select your database',
        ('Database Name')
    )
    table_selectbox = st.sidebar.selectbox(
        'Select your table',
        ('Table Name')
    )
    




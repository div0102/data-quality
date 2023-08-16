

import streamlit as st


class FileOptions():
    def __init__(self, file_type) -> None:
        self.file_type = file_type
        self.file_type = st.sidebar.selectbox("File type",("csv","excel"))

class CSV():
    def __init__(self) -> None:
        self.file_delimeter = st.sidebar.selectbox("File Delmiter",(',','|','\\t','--','*'))
        self.file_header = st.sidebar.selectbox("Does file have a header",("Yes","No"))
        self.uploaded_file = st.sidebar.file_uploader(label="Upload File", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        
    
class EXCEL(FileOptions):
    def __init__(self, ) -> None:
        self.uploaded_file = st.sidebar.file_uploader(label="Upload File", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.write("We don't support excel files yet. but its on our roadmap!")
    
        
    
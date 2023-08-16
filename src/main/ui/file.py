

import streamlit as st
from constants import BinarySelectionVal, FileDelimeters, FileTypes


class FileOptions():
    def __init__(self, file_type) -> None:
        self.file_type = file_type
        self.file_type = st.sidebar.selectbox("File type",(file_type.value for file_type in FileTypes))

class CSV():
    def __init__(self) -> None:
        self.file_delimeter = st.sidebar.selectbox("File Delmiter",(delimeter.value for delimeter in FileDelimeters))
        self.file_header = st.sidebar.selectbox("Does file have a header",(binary.value for binary in BinarySelectionVal))
        self.uploaded_file = st.sidebar.file_uploader(label="Upload File", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        
    
class EXCEL(FileOptions):
    def __init__(self, ) -> None:
        self.uploaded_file = st.sidebar.file_uploader(label="Upload File", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
        st.write("We don't support excel files yet. but its on our roadmap!")
    
        
    
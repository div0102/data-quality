from io import StringIO

import streamlit as st
from constants import SourceSystems
from source_factory.databases.snow import SourceSnowflake
from source_factory.file.f_csv import SourceCSV
from ui.dqc import list_all_supported_dq_frameworks
from ui.file import CSV, EXCEL, FileOptions

# st.set_page_config(
#     page_title="Ex-stream-ly Cool App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!"
#     }
# )

st.title("Configure your DQ checks here")
st.selectbox("DQ Framework Support", list_all_supported_dq_frameworks())
st.sidebar.markdown("# WUYDB source availabilty 🎈")
source = st.sidebar.selectbox(
    "Choose your source for DQ", (src_systems.value for src_systems in SourceSystems)
)
if source == "Local File":
    wrk_with_files = FileOptions(source)
    # file_type, uploaded_file = wrk_with_files.file_options()
    if wrk_with_files.file_type == "csv":
        csv = CSV()
        if csv.uploaded_file is not None:
            csv = SourceCSV(csv.uploaded_file, csv.file_header, csv.file_delimeter)
            csv_data = csv.read_file()
            csv.add_dq_checks_for_cols(csv_data)
            # headers = csv.fetch_file_headers(csv_data)
            # print(headers)
            # # headers= ['Id','Name','Salary']
            # for i in headers:
            #     print(i)
            #     st.checkbox(i)
            # st.write(headers)
            # st.write(csv.fetch_file_headers(csv_data))
            st.write("Sample Data", csv.show_sample_file_data(csv_data))
            # st.dataframe(data=csv.show_sample_file_data(csv_data))

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
            # dataframe = read_file(uploaded_file=uploaded_file)

            # headers = fetch_file_headers(dataframe)
            # print(headers)
            # headers= ['Id','Name','Salary']
            # for i in headers:
            #     print(i)
            #     st.checkbox(i)
            # st.write("Sample Data",dataframe)
            # st.write(headers)
            # st.write(fetch_file_headers(dataframe))
    if wrk_with_files.file_type == "excel":
        EXCEL()

    # file_type = st.sidebar.selectbox("File type",("csv","excel"))
    # file_delimeter = st.sidebar.selectbox("File Delmiter",(',','|','\\t','--','*'))
    # file_header = st.sidebar.selectbox("Does file have a header",("Yes","No"))
    # uploaded_file = st.sidebar.file_uploader(label="Upload File", type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
elif source == "Snowflake":
    from connection_factory.snowflake.conn_snow import snowConnection

    snow_manager = snowConnection("Snowflake".lower())
    connection_list = snow_manager.list_connection()
    print(connection_list)
    connection_list.insert(0, "available connections")
    print(connection_list)
    connection_selectbox = st.sidebar.selectbox(
        "Chosse the connection name", (connection_list), key="snow_connection_sb"
    )
    if connection_selectbox != "available connections":
        if st.sidebar.button(
            "Test connection",
            on_click=snow_manager.test_connection,
            args=[connection_selectbox],
            type="secondary",
        ):
            st.sidebar.text("Connection Successfull!")
        else:
            st.sidebar.text(
                "Couldn't establish a connection",
                help="Check snowflake connection details!!",
            )
        # create a snowflake connection object

        snow_conn_obj = snow_manager.load_connection(connection_selectbox)

        databse_list = snow_manager.show_databases(connection_selectbox)
        database_selectbox = st.sidebar.selectbox(
            "Select your database",
            (databse_list),
            key="snow_database_sb",
        )

        schema_list = snow_manager.show_schemas(snow_conn_obj, database_selectbox)
        schema_selectbox = st.sidebar.selectbox(
            "Select your schema", (schema_list), key="snow_schema_sb"
        )

        table_list = snow_manager.show_tables(
            snow_conn_obj, database_selectbox, schema_selectbox
        )
        table_selectbox = st.sidebar.selectbox(
            "Select your table", (table_list), key="snow_table_sb"
        )

        if table_selectbox:
            ui_snow = SourceSnowflake(
                snow_conn_obj, database_selectbox, schema_selectbox, table_selectbox
            )

            ui_snow.add_dq_checks_for_cols()
            if st.button("Sample Data"):
                st.write("Sample Data", ui_snow.show_sample_table_data())


if source in ["Database", "Bigquery"]:
    # Add a selectbox to the sidebar:
    database_selectbox = st.sidebar.selectbox("Select your database", ("Database Name"))
    table_selectbox = st.sidebar.selectbox("Select your table", ("Table Name"))

import snowflake.connector
from yaml import FullLoader, load


class snowConnection:
    def __init__(self, sourcename) -> None:
        self.sourcename = sourcename
        conn_detail_path = r"src\main\connection_factory\conn_configs\conn.yml"
        with open(conn_detail_path, "r") as stream:
            self.get_connection = load(stream, Loader=FullLoader)[
                self.sourcename
            ]  # ["snowflake"]

    def list_connection(self) -> list:
        """list all avialble connections for snowflake"""

        all_connections = [
            list(conn_name.keys())[0]
            for conn_name in self.get_connection["connection_name"]
        ]
        return all_connections  # list(.keys())

    def load_connection(self, connection_name: str):
        """Sets the connection object"""
        for conn_name in self.get_connection["connection_name"]:
            if connection_name in conn_name:
                conn_name = conn_name[connection_name]
                return snowflake.connector.connect(
                    user=conn_name["username"],
                    password=conn_name["password"],
                    account=conn_name["account"],
                    warehouse=conn_name["warehouse"],
                )

    def test_connection(self, connection_name: str):
        conn = self.load_connection(connection_name)
        test_sql = conn.cursor().execute("Select 1").fetchone()[0]
        if test_sql == 1:
            return "Connection Successful"
        return "Couldn't establish a connection"

    def show_databases(self, connection_name: str):
        conn = self.load_connection(connection_name)
        get_all_dbs = conn.cursor().execute("SHOW DATABASES").fetchall()
        return [dbs[1] for dbs in get_all_dbs]

    # f""" execute immediate $$ BEGIN USE DATABASE {database_name}; SHOW SCHEMAS; END; $$ """
    def show_schemas(self, connection, database_name: str):
        get_all_schemas = connection.cursor().execute("SHOW SCHEMAS").fetchall()

        return [
            schema[1]
            for schema in get_all_schemas
            if schema[4] == database_name.upper()
        ]

    def show_tables(self, connection, database_name: str, schema_name: str):
        get_all_tables = connection.cursor().execute("SHOW TABLES").fetchall()

        return [
            table[1]
            for table in get_all_tables
            if table[2] == database_name.upper() and table[3] == schema_name
        ]

    def get_table_columns(
        connection, database_name: str, schema_name: str, table_name: str
    ):
        get_col_sql = f"Select column_name from information_schema.columns where TABLE_CATALOG = '{database_name}' and TABLE_SCHEMA = '{schema_name}'\
        and TABLE_NAME = '{table_name}'"
        connection.cursor().execute(f"USE {database_name}.{schema_name};")
        get_all_columns = connection.cursor().execute(get_col_sql).fetchall()
        connection.close()
        return get_all_columns


# print(self.get_connection)
# print(list_connection())
# print(test_connection("wuydb"))
# print(show_databases("wuydb"))
# print(show_schemas(connection, "snowflake"))
# print(show_tables(connection, "SNOWFLAKE_SAMPLE_DATA", "TPCDS_SF100TCL"))
# print(
#     get_table_columns(
#         connection, "SNOWFLAKE_SAMPLE_DATA", "TPCDS_SF100TCL", "INVENTORY"
#     )
# )

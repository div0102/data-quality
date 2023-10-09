# from main.constants import SourceSystems

from snowflake.conn_snow import snowConnection

if SourceSystems.SNOWFLAKE.value == "Snowflake":
    snow_manager = snowConnection()
    print(snow_manager)

from enum import Enum


class SupportedDQCframeworks(Enum):
    LLM_CHAT_GPT = "GPT"
    OS_GREAT_EXPECTATIONS = "Great Expectations"

class DQC(Enum):
    MANDORTORY_VALUE_CHECK = 'Mandatory value check'
    DUPLICATE_CHECK = 'Duplicate check'
    NULL_CHECK = 'Null value check'
    DATE_FORMAT_CHECK = 'Date format check'
    SPECIAL_CHARACTER_CHECK = 'Special character check'

class SourceSystems(Enum):
    LOCAL_FILE = "Local File"
    SNOWFLAKE = "Snowflake"
    BIGQUERY = "BigQuery"
    AWS_S3 = "AWS_S3"
    GCP_GCS = "GCS"

class FileTypes(Enum):
    CSV = "csv"
    EXCEL = "excel"

class FileDelimeters(Enum):
    COMMA=","
    PIPE="|"
    ASTERIK="*"
    HYPHEN="-"
    TAB="\\t"
    SPACE="space"

class BinarySelectionVal(Enum):
    YES="Yes"
    NO="No"
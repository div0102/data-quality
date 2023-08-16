from enum import Enum


class DQC(Enum):
    MANDORTORY_VALUE_CHECK = 'Mandatory value check'
    DUPLICATE_CHECK = 'Duplicate check'
    NULL_CHECK = 'Null value check'
    DATE_FORMAT_CHECK = 'Date format check'
    SPECIAL_CHARACTER_CHECK = 'Special character check'
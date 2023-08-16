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


def list_all_dqc():
    return [ dqc_checks.value for dqc_checks in DQC]

def list_all_supported_dq_frameworks():
    return [frameworks.value for frameworks in SupportedDQCframeworks]
from constants import DQC, SupportedDQCframeworks


def list_all_dqc():
    return [ dqc_checks.value for dqc_checks in DQC]

def list_all_supported_dq_frameworks():
    return [frameworks.value for frameworks in SupportedDQCframeworks]
import yaml
from constants import DQC, SupportedDQCframeworks


def list_all_dqc():
    all_dqc = [dqc_checks.value for dqc_checks in DQC]
    all_dqc.insert(0, "select one")
    return all_dqc


def list_all_supported_dq_frameworks():
    return [frameworks.value for frameworks in SupportedDQCframeworks]


def generate_dqc_config(
    dqc_col_selection: dict, table_name: str, schema_name: str, database_name: str
):
    dqc_d = {
        "data_quality": {
            "table_name": table_name,
            "schema_name": schema_name,
            "database_name": database_name,
            "check": {},
        }
    }
    for col, dqc in dqc_col_selection.items():
        if dqc != "select one":
            if dqc in dqc_d["data_quality"]["check"]:
                dqc_d["data_quality"]["check"][dqc] = dqc_d["data_quality"][
                    "check"
                ].get(dqc) + [col]
            else:
                dqc_d["data_quality"]["check"][dqc] = [col]

    print(dqc_d)

    with open("test_df_to_yaml.yaml", "w") as file:
        documents = yaml.dump(
            dqc_d,
            file,
            default_flow_style=False,
        )


# print(
#     generate_dqc_config(
#         {
#             "C_PHONE": "Mandatory value check",
#             "C_COMMENT": "Mandatory value check",
#             "C_NATIONKEY": "select one",
#             "C_MKTSEGMENT": "Date format check",
#             "C_ADDRESS": "select one",
#             "C_ACCTBAL": "select one",
#             "C_CUSTKEY": "Duplicate check",
#             "C_NAME": "select one",
#         },
#         "As",
#     )
# )

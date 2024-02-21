# For details of what the various configuration settings are for see the
# configuration documentation at:
# https://github.com/IDEMSInternational/parenttext-pipeline/blob/main/docs/configuration.md

# Data sources, IDs of Google Sheets where the core date is stored.
# Specific for ZA.
localised_sheets = "13do_Qnc0VKC6Ao4N7YY3skUFKJMuwOixj2GyMVwnRLM"

# Shared with all deployments.
# Multiple content index for different types of content.
T_content_ID = "1hcH8pFdiHZN0UvZgyv3Zht9ARBTx-VXhNBI2o8L7fHU"
T_C_onboarding_ID = "12ddvTz_ZfC-9-b0yxjVrSzczciUUE3GosLUFeOLIv9I"
C_ltp_activities_ID = "1Jx7vOmdefzK62ao2nlJJVLMAIS8d-6r1G8qn0jG8gww"
T_delivery_ID = "1yf6T8FsNF5SIS7ktj05Wj7ha_Hkfrf66r63kfUWhJbI"
C_modules_teen_ID = "1ONmD9PF9rcno3ha3QpfrIR5EIvHuuEqJXF3T90rlZ78"
C_dictionaries_ID = "1uc4WOOlyHTEV8fUGb8nPCYcPj446TRtsV8fucrOCxC4"
C_home_activity_checkin_ID = "1qjjM2XfkvGVk38GL2OASNkTrXyXuDMAuMUAKmgHYt_s"
T_C_menu_ID = "1lf80mIiuv_F6xAa9j5zGvXas50WxdSsLj6vrPccGNwY"
C_goal_checkin_ID = "1gympuD5KdlAdDJSuaVQiXjWSwJxoDcA9K-oBRyKmS7o"
C_dev_asess_tool_ID = "1OhhQF5yarUDmaSl2tlt7eIT7wJ8bGwNFzI3BOplJYsc"
safeguarding = "1PHgUhJnZdE0lK6C9teK-hwA6Tf-6Pgj1_OVdxoTgVOA"

sources = [
    {
        "filename": "parenttext_all",
        "spreadsheet_ids": [
            localised_sheets,
            T_C_onboarding_ID,
            C_ltp_activities_ID,
            T_delivery_ID,
            C_modules_teen_ID,
            C_dictionaries_ID,
            C_home_activity_checkin_ID,
            T_C_menu_ID,
            C_goal_checkin_ID,
            T_content_ID,
            C_dev_asess_tool_ID,
            safeguarding
        ],
        # "archive": "parenttext_all.zip",
        "archive": "https://drive.usercontent.google.com/download?id=1YPPe5bH0IwHg7HSXI8HHvUX96_6ErDb4&export=download&authuser=0&confirm=t&uuid=c1bfa3ca-58af-4d96-853e-383a4f30646a&at=APZUnTWlK7BXD8tO9L5PK7wlNJOC:1698621035109",  # noqa: E501
        "crowdin_name": "text_for_translators",
        # "tags": [1, "delivery",1, "menu", 2,"south_africa"],
        "tags": [2, "south_africa", 3, "teen"],
        "split_no": 3
    },
]

redirect_flow_names = (
    '['
    '    "safeguarding_redirect_to_topic_all", '
    '    "safeguarding_redirect_to_topic_highrisk", '
    '    "safeguarding_redirect_to_topic_trigger"'
    ']'
)


def create_config():
    return {
        "ab_testing_sheet_id": "1i_oqiJYkeoMsYdeFOcKlvvjnNCEdQnZlsm17fgNvK0s",
        "add_selectors": "yes",
        "count_threshold": "3",
        "default_expiration": 1440,
        "eng_edits_sheet_id": "1Ab8H_s26EuOiS4nZ6HGADjD4CZw55586LL66fl8tEWI",
        "folder_within_repo": "translations/parent_text_v2",
        "languages": [
            {"language": "hau", "code": "ss"},
            {"language": "zul", "code": "zu"}
        ],
        "length_threshold": "18",
        "localisation_sheet_id": "1FfO-LLjodgEKaBVnn47QrvXaM68Cvui55FS1DKziA2c",
        "model": "models.parenttext_models",
        "qr_treatment": "reformat",
        "redirect_flow_names": redirect_flow_names,
        "select_phrases": "edits/select_phrases.json",
        "sg_flow_id": "b83315a6-b25c-413a-9aa0-953bf60f223c",
        "sg_flow_name": "safeguarding_wfr_interaction",
        "sg_sources": [
            {"key": "zul", "path": "excel_files/safeguarding zulu.xlsx"},
            {"key": "hau", "path": "excel_files/safeguarding swati.xlsx"}
        ],
        "sources": sources,
        "special_expiration": "edits/specific_expiration.json",
        "special_words": "edits/special_words.json",
        "translation_repo": "https://github.com/IDEMSInternational/plh-digital-content",
        "transl_edits_sheet_id": "1fCLPfiqHy1nLLqh1qyvd3zrziw5Tz3uQ6_e7CyuEW-E",
    }

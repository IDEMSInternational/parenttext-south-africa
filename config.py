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

# "filename" is how it will be generally named in the pipeline.
#
# "crowdin_name" will be the name of the file that is produced to send to the
# translators.
#
# "tags" are used to identify flows to be process. Possible values for tag 1:
#   onboarding
#   dev_assess
#   ltp_activity
#   home_activity_checkin
#   module
#   goal_checkin
#   safeguarding
#   menu
#   delivery
#
# "split_no" is used to divide the file at the final step to get it to a manageable
# size that can be uploaded to RapidPro.
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
            T_content_ID,C_dev_asess_tool_ID,
            safeguarding,
        ],
        "crowdin_name": "text_for_translators",
        # "tags": [1, "delivery",1, "menu", 2,"south_africa"],
        "tags": [2, "south_africa", 3, "teen"],
        "split_no": 3
    },
]

# Data used when modifying expiration times.
special_expiration = "./edits/specific_expiration.json"
default_expiration = "1440"

# Model that is used as part of the process when the data is extracted from sheets.
model = "models.parenttext_models"

# Languages that will be looked for to localize back into the flows, "language" is the
# 3-letter code used in RapidPro, "code" is the 2 letter code used in CrowdIn.
languages = [
    {"language": "hau", "code": "ss"},
    {"language": "zul", "code": "zu"}
]

# Location where translations are stored, at the moment pointing to a locally cloned
# repo, should maybe be adapted so we can provide a link to an online repo.
translation_repo = "https://github.com/IDEMSInternational/plh-digital-content"
folder_within_repo = "translations/parent_text_v2"

# Destination file for all files (including intermediary files and log files).
# Default is 'output'.
outputpath = "output"

# In one of the latter stages we have the option to modify the quick replies:
# 1 - We may want to remove the quick replies and add them to message text and give
#     numerical prompts to allow basic phone users to use the app - for this use
#     reference code "move"
# 2 - We may want to reformat the quick replies so that long ones are added to the
#     message text as above - for this use reference code "reformat"
# 3 - We may not want to do anything, for this use reference code "none"
qr_treatment = "reformat"

# This is the default phrase we want to add in if the quick replies are being moved to
# message text.
select_phrases = "./edits/select_phrases.json"

# If we are in scenario 1 above, we may wish to add some basic numerical quick
# replies back in, if so we need to specify add_selectors as True
add_selectors = "yes"

# Words we always want to keep as full quick replies are specified in this file.
special_words = "./edits/special_words.json"

# In scenario 2 we set limits on the number of quick replies and the length of the
# quick replies.
#   count_threshold (relates to number of quick replies)
#   length_threshold (relates to length of the longest quick reply)
# If the number of QRs is below or equal the count_threshold and the longest QR is
# shorter than or equal to the length_threshold then the QR are to be left in place
# the node will not be changed.
# In places where the QR are too long. We will make the changes to make the QRs
# numbers and add the number references to the message text as example 1.
count_threshold = "3"
length_threshold = "18"

# Google Sheet ID containing AB testing data.
# Same for all deployments.
ab_testing_sheet_ID = "1i_oqiJYkeoMsYdeFOcKlvvjnNCEdQnZlsm17fgNvK0s"
# South Africa specific.
localisation_sheet_ID = "1FfO-LLjodgEKaBVnn47QrvXaM68Cvui55FS1DKziA2c"

# Google Sheet ID containing dict edits data.
# Same for all deployments.
eng_edits_sheet_ID = "1Ab8H_s26EuOiS4nZ6HGADjD4CZw55586LL66fl8tEWI"
# South Africa specific.
transl_edits_sheet_ID = "1fCLPfiqHy1nLLqh1qyvd3zrziw5Tz3uQ6_e7CyuEW-E"

# Data used in safeguarding script.
SG_flow_ID = "b83315a6-b25c-413a-9aa0-953bf60f223c"
SG_flow_name = "safeguarding_wfr_interaction"

# Path to file containing translated safeguarding words.
SG_path = "./edits/safeguarding_words.json"

# Names of redirect flows to be modified as part of safeguarding process.
redirect_flow_names = (
    '['
    '    "safeguarding_redirect_to_topic_all", '
    '    "safeguarding_redirect_to_topic_highrisk", '
    '    "safeguarding_redirect_to_topic_trigger"'
    ']'
)

def create_config():
    return {
        "ab_testing_sheet_id": ab_testing_sheet_ID,
        "add_selectors": add_selectors,
        "count_threshold": count_threshold,
        "default_expiration": default_expiration,
        "eng_edits_sheet_id": eng_edits_sheet_ID,
        "folder_within_repo": folder_within_repo,
        "languages": languages,
        "length_threshold": length_threshold,
        "localisation_sheet_id": localisation_sheet_ID,
        "model": model,
        "qr_treatment": qr_treatment,
        "redirect_flow_names": redirect_flow_names,
        "select_phrases": select_phrases,
        "sg_flow_id": SG_flow_ID,
        "sg_flow_name": SG_flow_name,
        "sg_path": SG_path,
        "sources": sources,
        "special_expiration": special_expiration,
        "special_words": special_words,
        "translation_repo": translation_repo,
        "transl_edits_sheet_id": transl_edits_sheet_ID,
    }

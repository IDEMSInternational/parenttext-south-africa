# Data sources, ids of google sheets where the core date is stored, 
localised_sheets = "13do_Qnc0VKC6Ao4N7YY3skUFKJMuwOixj2GyMVwnRLM"
T_C_onboarding_ID = "12ddvTz_ZfC-9-b0yxjVrSzczciUUE3GosLUFeOLIv9I"
T_content_ID = "1hcH8pFdiHZN0UvZgyv3Zht9ARBTx-VXhNBI2o8L7fHU" #multiple content index for different types of content
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
# "crowdin_name" will be the name of the file that is produced to send to the translators
# tags are used to identify flows to be process
# "split_no" is used to divide the file at the final step to get it to a manageable size that can be uploaded to rapidpro
sources = [
    {"filename": "parenttext_onboarding",
     "spreadsheet_ids": [T_C_onboarding_ID],
     # Should be able to add the full list of sheets here but I was running into some sheet permission errors, hopefully will run ok on Chiara's account      
     #"spreadsheet_ids": [localised_sheets, T_C_onboarding_ID, T_content_ID, C_ltp_activities_ID, T_delivery_ID, C_modules_teen_ID, C_dictionaries_ID, C_home_activity_checkin_ID, T_C_menu_ID, C_goal_checkin_ID, C_dev_asess_tool_ID, safeguarding], 
     "crowdin_name": "text_for_translators",
     "tags": [1,"onboarding",2,"global"],
     "split_no": 2},
]

# Model that is used as part of the process when the data is extracted from excel
model = "models.parenttext_models"

# Languages that will be looked for to localize back into the flows, "language" is the 3 letter code used in RapidPro, "code" is the 2 letter code used in crowdin
languages = [
    {"language": "swa", "code": "ss"}
]

# Location where translations are stored, at the moment pointing to a locally cloned repo, should maybe be adapted so we can provide a link to an online repo
translation_repo = "../PLH-Digital-Content/translations/parent_text_v2"

# Desination file for all files (including intermediary files and log files)
outputpath = "./output"

# In one of the latter stages we have the option to modify the quick replies,
# 1 - We may want to remove the quick replies and add them to message text and give numerical prompts to allow basic phone users to use the app - for this use reference code "move"
# 2 - We may want to reformat the quick replies so that long ones are added to the message text as above - for this use reference code "reformat"
# 3 - We may not want to do anything, for this use reference code "none"
qr_treatment = "reformat"

# This is the default phrase we want to add in if the quick replies are being moved to message text
select_phrases = "./edits/select_phrases.json"

# If we are in scenario 1 above, we may wish to add some basic numerical quick replies back in, if so we need to specify add_selectors as "yes"
add_selectors = "yes"

# Some words we always want to keep as full quick replies, they are specified in this file
special_words = "./edits/special_words.json"

# In scenario 2 we set limits on the number of quick replies and the length of the quick replies. 
#   count_threshold (relates to number of quick replies)
#   length_threshold (relates to length of the longest quick reply)
# If the number of QRs is below or equal the count_threshold and the longest QR is shorter than or equal to the length_threshold then the QR are to be left in place the node will not be changed. 
# In places where the QR are too long. We will make the changes to make the QRs numbers and add the number references to the message text as example 1.
# Thresholds should be entered as strings
count_threshold = "10"
length_threshold = "100"

#Google sheet ID containing ab testing data
ab_testing_sheet_ID = "1i_oqiJYkeoMsYdeFOcKlvvjnNCEdQnZlsm17fgNvK0s"
localisation_sheet_ID = None
#localisation_sheet_ID = "1FfO-LLjodgEKaBVnn47QrvXaM68Cvui55FS1DKziA2c"
#I was running into access problems so have turned this off for now

#Google sheet ID containing dict edits data
dict_edits_sheet_ID = None
#dict_edits_sheet_ID = "1fCLPfiqHy1nLLqh1qyvd3zrziw5Tz3uQ6_e7CyuEW-E"
#I was running into access problems so have turned this off for now

#Google sheet ID containing safeguarding data
SG_sheet_ID = None
SG_flow_name = None

#Path to file containing translated safeguarding words
SG_path = None
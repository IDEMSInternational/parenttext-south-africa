from parenttext_core.config import core_spreadsheet_ids

# Data sources, ids of google sheets where the core date is stored, 
localised_sheets = "13do_Qnc0VKC6Ao4N7YY3skUFKJMuwOixj2GyMVwnRLM" #specific for ZA

all_spreadsheet_ids = core_spreadsheet_ids
all_spreadsheet_ids.append(localised_sheets)

# "filename" is how it will be generally named in the pipeline.
# "crowdin_name" will be the name of the file that is produced to send to the translators
# tags are used to identify flows to be process
# "split_no" is used to divide the file at the final step to get it to a manageable size that can be uploaded to rapidpro
sources = [
    {"filename": "parenttext_all",
     "spreadsheet_ids": all_spreadsheet_ids, 
     "crowdin_name": "text_for_translators",
     # possible values for tag 1: onboarding dev_assess ltp_activity home_activity_checkin module goal_checkin safeguarding menu delivery
     #"tags": [1, "delivery",1, "menu", 2,"south_africa"],
     "tags": [2,"south_africa"],
     "split_no": 3},
]

# Data used when modifying expiration times
special_expiration = "./edits/specific_expiration.json"
default_expiration = "1440"

# Model that is used as part of the process when the data is extracted from excel
model = "models.parenttext_models"

# Languages that will be looked for to localize back into the flows, "language" is the 3 letter code used in RapidPro, "code" is the 2 letter code used in crowdin
languages = [
    {"language": "hau", "code": "ss"},
    {"language": "zul", "code": "zu"}
]

# Location where translations are stored, at the moment pointing to a locally cloned repo, should maybe be adapted so we can provide a link to an online repo
translation_repo = "https://github.com/IDEMSInternational/plh-digital-content"
folder_within_repo = "translations/parent_text_v2"

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
count_threshold = "3"
length_threshold = "18"

#Google sheet ID containing ab testing data
localisation_sheet_ID = "1FfO-LLjodgEKaBVnn47QrvXaM68Cvui55FS1DKziA2c" #south africa specific

#Google sheet ID containing dict edits data
transl_edits_sheet_ID = "1fCLPfiqHy1nLLqh1qyvd3zrziw5Tz3uQ6_e7CyuEW-E" #south africa specific

#Data used in safeguarding script
SG_flow_ID = "b83315a6-b25c-413a-9aa0-953bf60f223c"
SG_flow_name = "safeguarding_wfr_interaction"

#Path to file containing translated safeguarding words
SG_path = "./edits/safeguarding_words.json"

#Names of redirect flows to be modified as part of safegurading process
redirect_flow_names = '["safeguarding_redirect_to_topic_all", "safeguarding_redirect_to_topic_highrisk", "safeguarding_redirect_to_topic_trigger"]'
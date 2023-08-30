import os
import subprocess
import sys
# sys.path.append('C:/Users/edmun/Code/parenttext-pipeline/src/parenttext_pipeline')
# from pipelines import run_pipeline
# leave in place for now, above code enables quick local testing

from parenttext_pipeline.pipelines import run_pipeline
from parenttext_core.config import core_spreadsheet_ids, ab_testing_sheet_ID, eng_edits_sheet_ID
from config import *

def main():
    
    run_pipeline(
        sources,
        special_expiration,
        default_expiration, 
        model, 
        languages, 
        translation_repo, 
        folder_within_repo,
        outputpath, 
        qr_treatment,
        select_phrases, 
        add_selectors,
        special_words,
        count_threshold,
        length_threshold, 
        ab_testing_sheet_ID, 
        localisation_sheet_ID, 
        eng_edits_sheet_ID,
        transl_edits_sheet_ID,
        SG_flow_ID, 
        SG_flow_name,
        SG_path,
        redirect_flow_names
        )
    
if __name__ == '__main__':    
    main()


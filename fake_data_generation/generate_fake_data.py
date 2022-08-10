"""
This file generates fake data randomly.
The purpose of this data is to test the running of the models and setup of the repo.
Field values are generated randomly independently of each other.
Instructions on how to run this file can be found in the README.md in this directory.
"""

import argparse
import json
import numpy as np
import pandas as pd
import random

# Get arguments from command line
# (If args are not specified default values will be used.)
parser = argparse.ArgumentParser(
    description="""The purpose of `generate_fake_data.py` is to create a `.csv` file with fake data with the following intended applications: 
    An example of how data needs to be formatted to be passed into the model and to test the setup and running of the repo."""
)

# Args to generate
parser.add_argument(
    "--number_of_records",
    "-nr",
    type=int,
    default=100,
    help="[int] Number of records to generate. Default is 100.",
)
parser.add_argument(
    "--filename",
    "-fn",
    type=str,
    default="fake_data",
    help="""[str] The name of the csv file saved at the end (do not add.csv).
    The default name is set to "fake_data". This will generate a file called "fake_data.csv" . """,
)

parser.add_argument(
    "--only_major_cases",
    "-mc",
    default=False,
    action="store_true",
    help=""" [False - no need to specify, True - specify by just including: --only_major_cases]
    If True all records generated will have major cases listed as "Y" if False cases will be a mix of "N" and "Y".""",
)

parser.add_argument(
    "--seed",
    "-s",
    default=None,
    type=int,
    help="[int] If specified will ensure result is reproducible. Default is set to None so will generate a different result each time.",
)

# Read arguments from the command line
args = parser.parse_args()

# Set seed if specified:
if args.seed is not None:
    np.random.seed(seed=args.seed)

# Load data_description.json to get columns required for training data
with open("../config/data_description.json", "r") as file:
    data_columns = json.load(file)

# Create dataframe with original data fields
columns = [x.upper() for x in data_columns["Original_Data_Fields"]]
df = pd.DataFrame(columns=columns)

# Load data_categories.json to get the data categories required for each field in the fake data
with open("../config/fake_data_categories.json", "r") as file:
    data_cat = json.load(file)

# Assign data categories to fields in dataframe
for column in columns:
    if column in data_cat.keys():
        df[column] = np.random.choice(data_cat[column], size=args.number_of_records)

# Remaining fields to fill in so they are not null
# fields requiring int:
df["LENGTH_OF_STAY"] = np.random.randint(1, 40, size=(args.number_of_records))
df["LENGTH_OF_STAY_IN_MINUTES"] = df["LENGTH_OF_STAY"] * 24 * 60
df["AGE_ON_ADMISSION"] = np.random.randint(18, 80, size=(args.number_of_records))
df["LOCAL_PATIENT_IDENTIFIER"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["CDS_UNIQUE_IDENTIFIER"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["PREVIOUS_30_DAY_HOSPITAL_PROVIDER_SPELL_NUMBER"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["ED_ATTENDANCE_EPISODE_NUMBER"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["UNIQUE_INTERNAL_ED_ADMISSION_NUMBER"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["UNIQUE_INTERNAL_IP_ADMISSION_NUMBER"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["AE_ATTENDANCE_CATEGORY"] = np.random.randint(1, 3, size=(args.number_of_records))
df["HEALTHCARE_RESOURCE_GROUP_CODE"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["PRESENTING_COMPLAINT_CODE"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["WAIT"] = np.random.randint(1, 3, size=(args.number_of_records))
df["ALL_INVESTIGATION_CODES"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["ALL_DIAGNOSIS_CODES"] = np.random.randint(1000, 2000, size=(args.number_of_records))
df["ALL_TREATMENT_CODES"] = np.random.randint(1000, 2000, size=(args.number_of_records))
df["ALL_BREACH_REASON_CODES"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["ALL_LOCATION_CODES"] = np.random.randint(1000, 2000, size=(args.number_of_records))
df["ALL_LOCAL_INVESTIGATION_CODES"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)

df["ALL_LOCAL_TREATMENT_CODES"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)

df["INITIAL_WAIT"] = np.random.randint(0, 600, size=(args.number_of_records))
df["WAIT"] = np.random.randint(0, 600, size=(args.number_of_records))
df["INITIAL_WAIT_MINUTES"] = np.random.randint(0, 600, size=(args.number_of_records))
df["WAIT_MINUTES"] = np.random.randint(0, 600, size=(args.number_of_records))


df["AE_PATIENT_GROUP_CODE"] = np.random.randint(
    1000, 2000, size=(args.number_of_records)
)
df["AE_INITIAL_ASSESSMENT_TRIAGE_CATEGORY"] = np.random.randint(
    1, 3, size=(args.number_of_records)
)
df["EMCOUNTLAST12M"] = np.random.choice([10, 20, 30], size=args.number_of_records)
df["EL COUNTLAST12M"] = np.random.choice([10, 20, 30], size=args.number_of_records)
df["ED COUNTLAST12M"] = np.random.choice([10, 20, 30], size=args.number_of_records)
df["OP FIRST COUNTLAST12M"] = np.random.choice(
    [10, 20, 30], size=args.number_of_records
)
df["OP FU COUNTLAST12M"] = np.random.choice([10, 20, 30], size=args.number_of_records)
# fields requiring str:
df["DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL"] = "2122-05-01"
df["DISCHARGE_READY_DATE"] = "2122-05-01"
df["EXPECTED_DISCHARGE_DATE"] = "2122-05-01"
df["EXPECTED_DISCHARGE_DATE_TIME"] = "2122-05-01"
df["FIRST_REGULAR_DAY_OR_NIGHT_ADMISSION_DESCRIPTION"] = "2122-05-01"
df["FIRST_START_DATE_TIME_WARD_STAY"] = "2122-05-01"
df["START_DATE_HOSPITAL_PROVIDER_SPELL"] = "2122-05-01"
df["START_DATE_TIME_HOSPITAL_PROVIDER_SPELL"] = "2122-05-01"
df["TREATMENT_FUNCTION_CODE_AT_ADMISSION_DESCRIPTION"] = "test"
df["PATIENT_GENDER_CURRENT_DESCRIPTION"] = "test"
df["ALL_DIAGNOSES"] = "test"
df["REASON_FOR_ADMISSION"] = "test"
df["ALL_INVESTIGATIONS"] = "test"
df["ALL_DIAGNOSIS"] = "test"
df["ALL_TREATMENTS"] = "test"
df["ALL_LOCAL_INVESTIGATIONS"] = "test"
df["ALL_LOCAL_TREATMENTS"] = "test"
df["PRESENTING_COMPLAINT"] = "test"
df["AE_PATIENT_GROUP"] = "test"
df["OAC GROUP NAME"] = "test"
df["OAC SUBGROUP NAME"] = "test"
df["OAC SUPERGROUP NAME"] = "test"
df["DISTRICT"] = "test"
df["FIRST_WARD_STAY_IDENTIFIER"] = "test"
df["MAIN_SPECIALTY_CODE_AT_ADMISSION_DESCRIPTION"] = "test"
df["PATIENT_CLASSIFICATION_DESCRIPTION"] = "test"
df["SOURCE_OF_ADMISSION_HOSPITAL_PROVIDER_SPELL_DESCRIPTION"] = "test"
df["POST_CODE_AT_ADMISSION_DATE_DISTRICT"] = "PostCode"
# fields requiring float:
df["IMD COUNTY DECILE"] = np.random.choice([0.1, 0.2, 0.3], size=args.number_of_records)

# Ensure all records only show "Y" for is "IS_MAJOR" if args.only_major_cases is True
if args.only_major_cases:
    df["IS_MAJOR"] = "Y"

# Rename fields to be as required for notebooksADMISSION,DISCHARGE_DATE_HOSPITAL_PROVIDER_SPELL,ETHNIC_CA
original_header = "LENGTH_OF_STAY,LENGTH_OF_STAY_IN_MINUTES,ADMISSION_METHOD_HOSPITAL_PROVIDER_SPELL_DESCRIPTION,AGE_ON_TEGORY_CODE_DESCRIPTION,DISCHARGE_READY_DATE,DIVISION_NAME_AT_ADMISSION,EXPECTED_DISCHARGE_DATE,EXPECTED_DISCHARGE_DATE_TIME,FIRST_REGULAR_DAY_OR_NIGHT_ADMISSION_DESCRIPTION,FIRST_START_DATE_TIME_WARD_STAY,FIRST_WARD_STAY_IDENTIFIER,IS_PATIENT_DEATH_DURING_SPELL,MAIN_SPECIALTY_CODE_AT_ADMISSION,MAIN_SPECIALTY_CODE_AT_ADMISSION_DESCRIPTION,PATIENT_CLASSIFICATION,PATIENT_CLASSIFICATION_DESCRIPTION,POST_CODE_AT_ADMISSION_DATE_DISTRICT,SOURCE_OF_ADMISSION_HOSPITAL_PROVIDER_SPELL,SOURCE_OF_ADMISSION_HOSPITAL_PROVIDER_SPELL_DESCRIPTION,START_DATE_HOSPITAL_PROVIDER_SPELL,START_DATE_TIME_HOSPITAL_PROVIDER_SPELL,TREATMENT_FUNCTION_CODE_AT_ADMISSION,TREATMENT_FUNCTION_CODE_AT_ADMISSION_DESCRIPTION,elective_or_non_elective,stroke_ward_stay,PATIENT_GENDER_CURRENT,PATIENT_GENDER_CURRENT_DESCRIPTION,LOCAL_PATIENT_IDENTIFIER,SpellDominantProcedure,all_diagnoses,cds_unique_identifier,previous_30_day_hospital_provider_spell_number,ED_attendance_episode_number,unique_internal_ED_admission_number,unique_internal_IP_admission_number,reason_for_admission,IS_care_home_on_admission,IS_care_home_on_discharge,ae_attendance_category,ae_arrival_mode,ae_attendance_disposal,ae_attendance_category_code,healthcare_resource_group_code,presenting_complaint_code,presenting_complaint,wait,wait_minutes,all_investigation_codes,all_diagnosis_codes,all_treatment_codes,all_breach_reason_codes,all_location_codes,all_investigations,all_diagnosis,all_treatments,all_local_investigation_codes,all_local_investigations,all_local_treatment_codes,all_local_treatments,attendance_type,initial_wait,initial_wait_minutes,major_minor,IS_major,ae_patient_group_code,ae_patient_group,ae_initial_assessment_triage_category_code,ae_initial_assessment_triage_category,manchester_triage_category,arrival_day_of_week,arrival_month_name,Illness Injury Flag,Mental Health Flag,Frailty Proxy,Presenting Complaint Group,IS_cancer,cancer_type,IS_chronic_kidney_disease,IS_COPD,IS_coronary_heart_disease,IS_dementia,IS_diabetes,diabetes_type,IS_frailty_proxy,IS_hypertension,IS_mental_health,IMD county decile,District,Rural urban classification,OAC Group Name,OAC Subgroup Name,OAC Supergroup Name,EMCountLast12m,EL CountLast12m,ED CountLast12m,OP First CountLast12m,OP FU CountLast12m"
renaming_dict = dict(zip(original_header.upper().split(","),original_header.split(",")))
df.rename(columns = renaming_dict,inplace=True)

# Write dataframe to csv
df.to_csv(f"../../data/raw/{args.filename}.csv", index=False)

# Message to show script has run
print(
    f"Fake Data Generated! File saved: {args.filename}.csv with {args.number_of_records} records created. Seed was set to {args.seed}."
)
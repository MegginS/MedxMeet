import requests
import json

def ct_payload():

    disease = 'OPMD AND oculopharyngeal muscular dystrophy'
    # to update disease per client
    num_results = '50'
    fmt = 'json'
    abt_fields = 'OrgFullName,OverallStatus,OfficialTitle,CompletionDate,BriefSummary,StudyType,'
    study_fields = 'PatientRegistry,MaximumAge,MinimumAge,'
    location_fields = 'LocationCity,LocationContactEMail,LocationContactName,LocationContactPhone,LocationCountry,LocationFacility,'
    contact_fields = 'CentralContactEMail,CentralContactName,CentralContactPhone,CentralContactPhoneExt,CentralContactRole'
    
    payload = {'expr': disease, 'fmt': fmt,'max_rnk': num_results, 'fields': abt_fields+study_fields+location_fields+contact_fields}
# 
    return payload


def add_to_study_info_dict(field_name, field_value, study_information, study):
    try:
        study_information[field_name] = study.get(field_value, 'Not Provided')[0]
    except IndexError:
        study_information[field_name] = ""


def check_clinical_trials():

    payload = ct_payload()

    ct_search = requests.get('https://ClinicalTrials.gov/api/query/study_fields', params= payload)
    ct_result = ct_search.json()
    all_studies = {}

    studies = ct_result.get('StudyFieldsResponse').get('StudyFields')
    i = 1

    for study in studies:
        study_information = {}
        add_to_study_info_dict("organization", 'OrgFullName', study_information, study)
        add_to_study_info_dict("status", 'OverallStatus', study_information, study)
        add_to_study_info_dict("title", 'OfficialTitle', study_information, study)
        add_to_study_info_dict("completion_date", 'CompletionDate', study_information, study)
        add_to_study_info_dict("summary", 'BriefSummary', study_information, study)
        add_to_study_info_dict("study_type", 'StudyType', study_information, study)
        add_to_study_info_dict("patient_registry", 'PatientRegistry', study_information, study)
        add_to_study_info_dict("max_age", 'MaximumAge', study_information, study)
        add_to_study_info_dict("min_age", 'MinimumAge', study_information, study)
        add_to_study_info_dict("city", 'LocationCity', study_information, study)
        add_to_study_info_dict("location_email", 'LocationContactEMail', study_information, study)
        add_to_study_info_dict("location_contact", 'LocationContactName', study_information, study)
        add_to_study_info_dict("location_phone", 'LocationContactPhone', study_information, study)
        add_to_study_info_dict("location_country", 'LocationCountry', study_information, study)
        add_to_study_info_dict("location_facility", 'LocationFacility', study_information, study)
        add_to_study_info_dict("contact_email", 'CentralContactEMail', study_information, study)
        add_to_study_info_dict("contact_name", 'CentralContactName', study_information, study)
        add_to_study_info_dict("contact_phone", 'CentralContactPhone', study_information, study)
        add_to_study_info_dict("contact_ext", 'CentralContactPhoneExt', study_information, study)
        add_to_study_info_dict("contact_role", 'CentralContactRole', study_information, study)

        all_studies[f'study{i}'] = study_information
        i += 1

    return json.dumps(all_studies)
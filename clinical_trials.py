import requests
import json

def ct_payload():

    disease = 'OPMD AND oculopharyngeal muscular dystrophy'
    num_results = '10'
    fmt = 'json'
    abt_fields = 'OrgFullName,OverallStatus,OfficialTitle,CompletionDate,BriefSummary,StudyType,'
    study_fields = 'PatientRegistry,MaximumAge,MinimumAge,'
    location_fields = 'LocationCity,LocationContactEMail,LocationContactName,LocationContactPhone,LocationCountry,LocationFacility,'
    contact_fields = 'CentralContactEMail,CentralContactName,CentralContactPhone,CentralContactPhoneExt,CentralContactRole'
    
    payload = {'expr': disease, 'fmt': fmt,'max_rnk': num_results, 'fields': abt_fields+study_fields+location_fields+contact_fields}
# 
    return payload


def clinical_trials():

    payload = ct_payload()

    ct_search = requests.get('https://ClinicalTrials.gov/api/query/study_fields', params= payload)
    ct_result = ct_search.json()
    print(ct_result)

   
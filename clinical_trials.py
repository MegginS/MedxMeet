import requests
import json

def ct_payload():

    disease = 'OPMD AND oculopharyngeal muscular dystrophy'
    num_results = '2'
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
    print(ct_result.get('StudyFieldsResponse').get('StudyFields'))

    studies = ct_result.get('StudyFieldsResponse').get('StudyFields')

    for study in studies:
        organization = study.get('OrgFullName', 'Not Provided')
        status = study.get('OverallStatus', 'Not Provided')
        title = study.get('OfficialTitle', 'Not Provided')
        completion_date = study.get('CompletionDate', 'Not Provided')
        summary = study.get('BriefSummary', 'Not Provided')
        study_type = study.get('StudyType', 'Not Provided')
        patient_registry = study.get('PatientRegistry', 'Not Provided')
        max_age = study.get('MaximumAge', 'Not Provided')
        min_age = study.get('MinimumAge', 'Not Provided')
        city = study.get('LocationCity', 'Not Provided')
        location_email = study.get('LocationContactEMail', 'Not Provided')
        location_contact = study.get('LocationContactName', 'Not Provided')
        location_phone = study.get('LocationContactPhone', 'Not Provided')
        location_country = study.get('LocationCountry', 'Not Provided')
        location_facility = study.get('LocationFacility', 'Not Provided')
        contact_email = study.get('CentralContactEMail', 'Not Provided')
        contact_name = study.get('CentralContactName', 'Not Provided')
        contact_phone = study.get('CentralContactPhone', 'Not Provided')
        contact_ext = study.get('CentralContactPhoneExt', 'Not Provided')
        contact_role = study.get('CentralContactRole', 'Not Provided')

        print(organization)
        print(status)
        print(title)
        print(completion_date)
        print(summary)
        print(study_type)
        print(patient_registry)
        print(max_age)
        print(min_age)
        print(city)
        print(location_email)
        print(location_contact)
        print(location_phone)
        print(location_country)
        print(location_facility)
        print(contact_email)
        print(contact_name)
        print(contact_phone)
        print(contact_ext)
        print(contact_role)
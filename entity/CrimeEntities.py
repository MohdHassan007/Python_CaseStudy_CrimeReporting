# entity/CrimeEntities.py

class Incident:
    def __init__(self, incident_type, incident_date, location, description, status, victim_id, suspect_id):
        self.__incident_id = None  # Let the database handle the auto-increment
        self.__incident_type = incident_type
        self.__incident_date = incident_date
        self.__location = location
        self.__description = description
        self.__status = status
        self.__victim_id = victim_id
        self.__suspect_id = suspect_id

    def __str__(self):
        return f"Incident(ID: {self.__incident_id}, Type: {self.__incident_type}, Date: {self.__incident_date}, " \
               f"Location: {self.__location}, Description: {self.__description}, Status: {self.__status}, " \
               f"VictimID: {self.__victim_id}, SuspectID: {self.__suspect_id})"
    def get_incident_id(self):
        return self.__incident_id

    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def get_incident_type(self):
        return self.__incident_type

    def set_incident_type(self, incident_type):
        self.__incident_type = incident_type

    def get_incident_date(self):
        return self.__incident_date

    def set_incident_date(self, incident_date):
        self.__incident_date = incident_date

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_victim_id(self):
        return self.__victim_id

    def set_victim_id(self, victim_id):
        self.__victim_id = victim_id

    def get_suspect_id(self):
        return self.__suspect_id

    def set_suspect_id(self, suspect_id):
        self.__suspect_id = suspect_id


class Victim:
    def __init__(self, first_name, last_name, date_of_birth, gender, contact_info):
        self.__victim_id = None  # Let the database handle the auto-increment
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__contact_info = contact_info

    def __str__(self):
        return f"Victim(ID: {self.__victim_id}, Name: {self.__first_name} {self.__last_name}, " \
               f"DOB: {self.__date_of_birth}, Gender: {self.__gender}, ContactInfo: {self.__contact_info})"
    def get_victim_id(self):
        return self.__victim_id

    def set_victim_id(self, victim_id):
        self.__victim_id = victim_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info


class Suspect:
    def __init__(self, first_name, last_name, date_of_birth, gender, contact_info):
        self.__suspect_id = None  # Let the database handle the auto-increment
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__contact_info = contact_info

    def __str__(self):
        return f"Suspect(ID: {self.__suspect_id}, Name: {self.__first_name} {self.__last_name}, " \
               f"DOB: {self.__date_of_birth}, Gender: {self.__gender}, ContactInfo: {self.__contact_info})"
    def get_suspect_id(self):
        return self.__suspect_id

    def set_suspect_id(self, suspect_id):
        self.__suspect_id = suspect_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info


class LawEnforcementAgency:
    def __init__(self, agency_name, jurisdiction, contact_info):
        self.__agency_id = None  # Let the database handle the auto-increment
        self.__agency_name = agency_name
        self.__jurisdiction = jurisdiction
        self.__contact_info = contact_info

    def __str__(self):
        return f"LawEnforcementAgency(ID: {self.__agency_id}, Name: {self.__agency_name}, " \
               f"Jurisdiction: {self.__jurisdiction}, ContactInfo: {self.__contact_info})"


    def get_agency_id(self):
        return self.__agency_id

    def set_agency_id(self, agency_id):
        self.__agency_id = agency_id

    def get_agency_name(self):
        return self.__agency_name

    def set_agency_name(self, agency_name):
        self.__agency_name = agency_name

    def get_jurisdiction(self):
        return self.__jurisdiction

    def set_jurisdiction(self, jurisdiction):
        self.__jurisdiction = jurisdiction

    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info


class Officer:
    def __init__(self, first_name, last_name, badge_number, rank, contact_info, agency_id):
        self.__officer_id = None  # Let the database handle the auto-increment
        self.__first_name = first_name
        self.__last_name = last_name
        self.__badge_number = badge_number
        self.__rank = rank
        self.__contact_info = contact_info
        self.__agency_id = agency_id

    def __str__(self):
        return f"Officer(ID: {self.__officer_id}, Name: {self.__first_name} {self.__last_name}, " \
               f"BadgeNumber: {self.__badge_number}, Rank: {self.__rank}, ContactInfo: {self.__contact_info}, " \
               f"AgencyID: {self.__agency_id})"

    def get_officer_id(self):
        return self.__officer_id

    def set_officer_id(self, officer_id):
        self.__officer_id = officer_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_badge_number(self):
        return self.__badge_number

    def set_badge_number(self, badge_number):
        self.__badge_number = badge_number

    def get_rank(self):
        return self.__rank

    def set_rank(self, rank):
        self.__rank = rank

    def get_contact_info(self):
        return self.__contact_info

    def set_contact_info(self, contact_info):
        self.__contact_info = contact_info

    def get_agency_id(self):
        return self.__agency_id

    def set_agency_id(self, agency_id):
        self.__agency_id = agency_id


class Evidence:
    def __init__(self, description, location_found, incident_id):
        self.__evidence_id = None  # Let the database handle the auto-increment
        self.__description = description
        self.__location_found = location_found
        self.__incident_id = incident_id

    def __str__(self):
        return f"Evidence(ID: {self.__evidence_id}, Description: {self.__description}, " \
               f"LocationFound: {self.__location_found}, IncidentID: {self.__incident_id})"

    def get_evidence_id(self):
        return self.__evidence_id

    def set_evidence_id(self, evidence_id):
        self.__evidence_id = evidence_id

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_location_found(self):
        return self.__location_found

    def set_location_found(self, location_found):
        self.__location_found = location_found

    def get_incident_id(self):
        return self.__incident_id

    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id


class Report:
    def __init__(self, incident_id, reporting_officer, report_date, report_details, status):
        self.__report_id = None  # Let the database handle the auto-increment
        self.__incident_id = incident_id
        self.__reporting_officer = reporting_officer
        self.__report_date = report_date
        self.__report_details = report_details
        self.__status = status

    def __str__(self):
        return f"Report(ID: {self.__report_id}, IncidentID: {self.__incident_id}, " \
               f"ReportingOfficer: {self.__reporting_officer}, ReportDate: {self.__report_date}, " \
               f"ReportDetails: {self.__report_details}, Status: {self.__status})"


    def get_report_id(self):
        return self.__report_id

    def set_report_id(self, report_id):
        self.__report_id = report_id

    def get_incident_id(self):
        return self.__incident_id

    def set_incident_id(self, incident_id):
        self.__incident_id = incident_id

    def get_reporting_officer(self):
        return self.__reporting_officer

    def set_reporting_officer(self, reporting_officer):
        self.__reporting_officer = reporting_officer

    def get_report_date(self):
        return self.__report_date

    def set_report_date(self, report_date):
        self.__report_date = report_date

    def get_report_details(self):
        return self.__report_details

    def set_report_details(self, report_details):
        self.__report_details = report_details

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

class Case:
    def __init__(self, case_id, case_description):
        self.__case_id = case_id
        self.__case_description = case_description

    def __str__(self):
        return f"Case(ID: {self.__case_id}, Description: {self.__case_description})"

    def get_case_id(self):
        return self.__case_id

    def get_case_description(self):
        return self.__case_description

    def set_case_description(self, case_description):
        self.__case_description = case_description
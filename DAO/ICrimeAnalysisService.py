# dao/ICrimeAnalysisService.py

from entity.CrimeEntities import Incident, Report
class ICrimeAnalysisService:
    def create_incident(self, incident):
        pass

    def update_incident_status(self, status, incident_id):
        pass

    def get_incidents_in_date_range(self, start_date, end_date):
        pass

    def search_incidents(self, criteria):
        pass

    def generate_incident_report(self, incident):
        pass

    def create_case(self, case_description, incidents):
        pass

    def get_case_details(self, case_id):
        pass

    def update_case_details(self, case):
        pass

    def get_all_cases(self):
        pass

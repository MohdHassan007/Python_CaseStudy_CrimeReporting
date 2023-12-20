# main/MainModule.py

from DAO.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl

from entity.CrimeEntities import Incident, Case, Report
from exception.CrimeExceptions import IncidentNumberNotFoundException

class MainModule:
    def __init__(self):
        self.crime_service = CrimeAnalysisServiceImpl()

    def run_menu(self):
        while True:
            print("\nCrime Analysis and Reporting System")
            print("1. Create Incident")
            print("2. Update Incident Status")
            print("3. Get Incidents within Date Range")
            print("4. Search Incidents by Type")
            print("5. Generate Incident Report")
            print("6. Create Case")
            print("7. Get Case Details")
            print("8. Update Case Details")
            print("9. Get All Cases")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                # Example: Create Incident
                incident = self.create_incident()
                print("Incident created:", incident)

            elif choice == "2":
                # Example: Update Incident Status
                self.update_incident_status()

            elif choice == "3":
                # Example: Get Incidents within Date Range
                self.get_incidents_within_date_range()

            elif choice == "4":
                # Example: Search Incidents by Type
                self.search_incidents_by_type()

            elif choice == "5":
                # Example: Generate Incident Report
                self.generate_incident_report()

            elif choice == "6":
                # Example: Create Case
                self.create_case()

            elif choice == "7":
                # Example: Get Case Details
                self.get_case_details()

            elif choice == "8":
                # Example: Update Case Details
                self.update_case_details()

            elif choice == "9":
                # Example: Get All Cases
                self.get_all_cases()

            elif choice == "0":
                print("Exiting the application. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    def create_incident(self):
        incident_type = input("Enter incident type: ")
        incident_date = input("Enter incident date (YYYY-MM-DD): ")
        location = input("Enter location: ")
        description = input("Enter description: ")
        status = input("Enter status (Open, Closed, Under Investigation): ")
        victim_id = int(input("Enter victim ID: "))
        suspect_id = int(input("Enter suspect ID: "))

        incident = Incident(incident_type, incident_date, location, description, status, victim_id, suspect_id)
        created = self.crime_service.create_incident(incident)

        if created:
            print("Incident created successfully!")
            return incident
        else:
            print("Failed to create incident.")

    def update_incident_status(self):
        incident_id = int(input("Enter incident ID to update status: "))
        new_status = input("Enter new status: ")

        updated = self.crime_service.update_incident_status(new_status, incident_id)

        if updated:
            print("Incident status updated successfully!")
        else:
            print("Failed to update incident status.")

    def get_incidents_within_date_range(self):
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        incidents = self.crime_service.get_incidents_in_date_range(start_date, end_date)

        if incidents:
            print("Incidents within date range:")
            for incident in incidents:
                print(incident)
        else:
            print("No incidents found within the specified date range.")

    def search_incidents_by_type(self):
        incident_type = input("Enter incident type to search: ")

        incidents = self.crime_service.search_incidents(incident_type)

        if incidents:
            print(f"Incidents of type {incident_type}:")
            for incident in incidents:
                print(incident)
        else:
            print(f"No incidents found for type {incident_type}.")

    def generate_incident_report(self):
        try:
            incident_id = int(input("Enter incident ID to generate report: "))
            reporting_officer = input("Enter reporting officer's id: ")
            report_date = input("Enter report date (YYYY-MM-DD): ")
            report_details = input("Enter report details: ")
            status = input("Enter report status (Draft, Finalized): ")
        except ValueError:
            print("Invalid input. Please enter valid data.")
            return

        incident = self.crime_service.get_incident_details(incident_id)

        if incident:
            report = Report(incident.get_incident_id(), reporting_officer, report_date, report_details, status)
            generated_report = self.crime_service.generate_incident_report(report)

            if generated_report:
                print("Incident Report generated:")
                print(generated_report)
            else:
                print("Failed to generate incident report.")
        else:
            print(f"No incident found with ID {incident_id}.")

    def create_case(self):
        case_description = input("Enter case description: ")

        incident_ids = input("Enter incident IDs (comma-separated): ")
        incident_ids = [int(id.strip()) for id in incident_ids.split(',')]

        incidents = [self.crime_service.get_incident_details(incident_id) for incident_id in incident_ids]

        if all(incidents):
            case = Case(case_description, incidents)
            created = self.crime_service.create_case(case_description, incidents)

            if created:
                print("Case created successfully!")
            else:
                print("Failed to create case.")
        else:
            print("One or more incidents not found.")

    def get_case_details(self):
        case_id = int(input("Enter case ID: "))

        case = self.crime_service.get_case_details(case_id)

        if case:
            print("Case details:")
            print(case)
        else:
            print(f"No case found with ID {case_id}.")

    def update_case_details(self):
        try:

            case_id = int(input("Enter case ID to update details: "))
            new_description = input("Enter new case description: ")
            # Print for debugging
            print("Updating case details in service:")
            print(f"Case ID: {case_id}")
            print(f"New Description: {new_description}")

            case = Case(case_description=new_description, case_id=case_id)
            updated = self.crime_service.update_case_details(case)

            # Print for debugging
            print(f"Updated in service: {updated}")

            return updated

        except Exception as e:
            print(f"Error in service: {e}")
            return False

    def get_all_cases(self):
        cases = self.crime_service.get_all_cases()

        if cases:
            print("All cases:")
            for case in cases:
                print(case)
        else:
            print("No cases found.")

if __name__ == "__main__":
    main_module = MainModule()
    main_module.run_menu()

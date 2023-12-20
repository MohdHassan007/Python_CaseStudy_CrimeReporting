# dao/CrimeAnalysisServiceImpl.py

import mysql.connector
from mysql.connector import Error
from entity.CrimeEntities import Incident, Report, Case
from util.DBConnUtil import DBConnUtil
from exception.CrimeExceptions import IncidentNumberNotFoundException


class CrimeAnalysisServiceImpl:
    def __init__(self):
        self.connection = DBConnUtil.open_connection()


    def create_incident(self, incident):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to insert incident into the database
            query = "INSERT INTO Incidents (IncidentType, IncidentDate, Location, Description, Status, VictimID, SuspectID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (incident.get_incident_type(), incident.get_incident_date(), incident.get_location(),
                      incident.get_description(), incident.get_status(), incident.get_victim_id(),
                      incident.get_suspect_id())

            cursor.execute(query, values)

            self.connection.commit()
            cursor.close()

            return True

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False

    def update_incident_status(self, status, incident_id):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to update incident status in the database
            query = "UPDATE Incidents SET Status = %s WHERE IncidentID = %s"
            values = (status, incident_id)

            cursor.execute(query, values)

            self.connection.commit()
            cursor.close()

            return True

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False

    def get_incidents_in_date_range(self, start_date, end_date):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to retrieve incidents within a date range from the database
            query = "SELECT * FROM Incidents WHERE IncidentDate BETWEEN %s AND %s"
            values = (start_date, end_date)

            cursor.execute(query, values)
            incidents = []

            for row in cursor.fetchall():
                incident = Incident(
                    row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
                incident.set_incident_id(row[0])
                incidents.append(incident)

            cursor.close()
            return incidents

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return []

    def search_incidents(self, criteria):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to search for incidents based on various criteria in the database
            query = "SELECT * FROM Incidents WHERE IncidentType = %s"
            values = (criteria,)

            cursor.execute(query, values)
            incidents = []

            for row in cursor.fetchall():
                incident = Incident(
                    row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
                incident.set_incident_id(row[0])
                incidents.append(incident)

            cursor.close()
            return incidents

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return []

    def generate_incident_report(self, report):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to generate an incident report in the database
            query = "INSERT INTO Reports (IncidentID, ReportingOfficer, ReportDate, ReportDetails, Status) VALUES (%s, %s, %s, %s, %s)"
            values = (report.get_incident_id(), report.get_reporting_officer(), report.get_report_date(),
                      report.get_report_details(), report.get_status())

            cursor.execute(query, values)

            self.connection.commit()
            cursor.close()

            # Assuming you want to return the generated report
            return report

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None

    def create_case(self, case_description, incidents):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to create a case and associate it with incidents in the database
            query = "INSERT INTO Cases (CaseDescription) VALUES (%s)"
            values = (case_description,)

            cursor.execute(query, values)

            case_id = cursor.lastrowid

            # Associate incidents with the case
            for incident in incidents:
                query = "INSERT INTO CaseIncidents (CaseID, IncidentID) VALUES (%s, %s)"
                values = (case_id, incident.get_incident_id())
                cursor.execute(query, values)

            self.connection.commit()
            cursor.close()

            # Assuming you want to return the created case
            return Case(case_id, case_description)

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None

    def get_case_details(self, case_id):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to retrieve details of a specific case from the database
            query = "SELECT * FROM Cases WHERE CaseID = %s"
            values = (case_id,)

            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                case = Case(result[0], result[1])
            else:
                case = None

            cursor.close()
            return case

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None

    def update_case_details(self, case):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to update case details in the database
            query = "UPDATE Cases SET CaseDescription = %s WHERE CaseID = %s"
            values = (case.get_case_description(), case.get_case_id())

            cursor.execute(query, values)

            self.connection.commit()
            cursor.close()

            return True

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False

    def get_all_cases(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT * FROM Cases"
            cursor.execute(query)
            cases = []

            for row in cursor.fetchall():
                case = Case(row[0], row[1])
                cases.append(case)

            cursor.close()
            return cases
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return []

    def get_incident_details(self, incident_id):
        try:
            cursor = self.connection.cursor()

            # Implement the logic to retrieve details of a specific incident from the database
            query = "SELECT * FROM Incidents WHERE IncidentID = %s"
            values = (incident_id,)

            cursor.execute(query, values)
            result = cursor.fetchone()

            if result:
                incident = Incident(result[1], result[2], result[3], result[4], result[5], result[6], result[7])
                incident.set_incident_id(result[0])
                return incident
            else:
                raise IncidentNumberNotFoundException(f"Incident with ID {incident_id} not found")

        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return None
        except IncidentNumberNotFoundException as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()

import unittest
import mysql.connector
from DAO.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl  # Adjust the import based on your project structure
from entity.CrimeEntities import Incident  # Adjust the import based on your project structure

class TestCrimeAnalysisService(unittest.TestCase):
    def setUp(self):
        # Set up a test MySQL database connection
        self.connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='123456789',
            database='PythonTest'
        )
        self.crime_service = CrimeAnalysisServiceImpl()
        self.crime_service.connection = self.connection

        # Create a table for testing


    def test_create_incident(self):
        # Test data
        incident = Incident('homicide', '2023-01-01', 'Hyderabad', 'description', 'Open', 3, 2)

        # Calling the method
        created = self.crime_service.create_incident(incident)

        # Assertions
        self.assertTrue(created)

        # Check if the data is inserted into the database
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT * FROM incidents')
            result = cursor.fetchone()
            self.assertEqual(result['IncidentType'], 'homicide')
            # Add more assertions for other fields
            cursor.fetchall()

    def test_update_incident_status(self):
        # Test data
        incident_id = 1
        status = 'Closed'
        # Insert a sample record for testing
       # with self.connection.cursor() as cursor:
        #    cursor.execute('''
       #         INSERT INTO incidents (Incidenttype, Incidentdate, location, description, status, victimID, suspectID)
        #        VALUES ('homicide', '2023-01-01', 'Hyderabad', 'description', 'Open', 3, 2)
       #    ''')

        # Calling the method
        updated = self.crime_service.update_incident_status(status, incident_id)

        # Assertions
        self.assertTrue(updated)

        # Check if the status is updated in the database
        with self.connection.cursor(dictionary=True) as cursor:
            cursor.execute('SELECT status FROM incidents WHERE IncidentID = %s', (incident_id,))
            result = cursor.fetchone()
            self.assertEqual(result['status'], 'Closed')

    def tearDown(self):
        # Close the connection
        self.connection.close()

if __name__ == '__main__':
    unittest.main()

import unittest
from DAO.CrimeAnalysisServiceImpl import CrimeAnalysisServiceImpl  # Adjust the import based on your project structure
from entity.CrimeEntities import Incident  # Adjust the import based on your project structure
from unittest.mock import MagicMock


class TestCrimeAnalysisService(unittest.TestCase):
    def setUp(self):
        # Mocking the DB connection
        self.mock_connection = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_connection.cursor.return_value = self.mock_cursor
        self.crime_service = CrimeAnalysisServiceImpl()
        self.crime_service.connection = self.mock_connection  # Assign the mock connection

    def test_create_incident(self):
        # Mocking the execute method
        self.mock_cursor.execute.return_value = True

        # Test data
        incident = Incident('homicide', '2023-01-01', 'Hyderabad', 'description', 'Open', 3, 2)

        # Calling the method
        created = self.crime_service.create_incident(incident)

        # Assertions
        self.assertTrue(created)
        self.assertTrue(self.mock_connection.commit.called)

    def test_update_incident_status(self):
        # Mocking the execute method
        self.mock_cursor.execute.return_value = True

        # Test data
        incident_id = 1
        status = 'Closed'

        # Calling the method
        updated = self.crime_service.update_incident_status(status, incident_id)

        # Assertions
        self.assertTrue(updated)
        self.assertTrue(self.mock_connection.commit.called)

if __name__ == '__main__':
    unittest.main()

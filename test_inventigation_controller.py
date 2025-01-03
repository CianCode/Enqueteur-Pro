import unittest
from unittest.mock import MagicMock
from src.controllers.investigation_controller import InvestigationController

class TestInvestigationController(unittest.TestCase):

    def setUp(self):
        """Setup the InvestigationController with a mocked DatabaseController."""
        self.controller = InvestigationController()
        self.controller.db = MagicMock()


    def test_delete_investigation(self):
        """Test the delete_investigation method."""
        self.controller.delete_investigation(1)
        self.controller.db.execute_query.assert_called_with(
            "DELETE FROM Investigation WHERE id_investigation = %s;",
            (1,)
        )

    def test_list_investigations(self):
        """Test the list_investigations method."""
        self.controller.db.execute_query.return_value = [(1, "Investigation 1", "open")]
        result = self.controller.list_investigations()
        self.assertEqual(result, [(1, "Investigation 1", "open")])
        self.controller.db.execute_query.assert_called_with(
            "SELECT * FROM Investigation;",
            fetch_results=True
        )

    def test_get_investigation_by_id(self):
        """Test the get_investigation_by_id method."""
        self.controller.db.execute_query.return_value = [(1, "Investigation 1", "open")]
        result = self.controller.get_investigation_by_id(1)
        self.assertEqual(result, (1, "Investigation 1", "open"))
        self.controller.db.execute_query.assert_called_with(
            "SELECT * FROM Investigation WHERE id_investigation = %s;",
            (1,),
            fetch_results=True
        )

    def test_list_investigation_for_reports(self):
        """Test the list_investigation_for_reports method."""
        self.controller.db.execute_query.return_value = [(1, "Report 1", "2025-01-01")]
        result = self.controller.list_investigation_for_reports(1)
        self.assertEqual(result, [(1, "Report 1", "2025-01-01")])
        self.controller.db.execute_query.assert_called_with(
            "SELECT * FROM Report WHERE investigation_relation = %s;",
            (1,),
            fetch_results=True
        )

    def test_get_crime_type_label(self):
        """Test the get_crime_type_label method."""
        self.controller.db.execute_query.return_value = [("Robbery",)]
        result = self.controller.get_crime_type_label(1)
        self.assertEqual(result, "Robbery")
        self.controller.db.execute_query.assert_called_with(
            "SELECT label FROM TypeCrime WHERE id_crime = %s;",
            (1,),
            fetch_results=True
        )

if __name__ == "__main__":
    unittest.main()

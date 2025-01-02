import unittest
from unittest.mock import MagicMock
from src.controllers.evidence_controller import EvidenceController

class TestEvidenceController(unittest.TestCase):
    def setUp(self):
        # Initialize the EvidenceController with a mock DatabaseController
        self.evidence_controller = EvidenceController()
        self.evidence_controller.db = MagicMock()



    def test_delete_evidence(self):
        # Call the method
        self.evidence_controller.delete_evidence(1)

        # Assertions
        self.evidence_controller.db.execute_query.assert_called_with(
            "DELETE FROM Evidence WHERE id_evidence = %s;",
            (1,)
        )


    def test_update_evidence_with_description(self):
        # Call the method
        self.evidence_controller.update_evidence(1, description="Updated description")

        # Assertions
        self.evidence_controller.db.execute_query.assert_called_with(
            """
            UPDATE Evidence
            SET description = %s
            WHERE id_evidence = %s;
            """,
            ("Updated description", 1)
        )

    def test_update_evidence_with_both_fields(self):
        # Call the method
        self.evidence_controller.update_evidence(1, description="Updated description", type_evidence_id=2)

        # Assertions
        self.evidence_controller.db.execute_query.assert_called_with(
            """
            UPDATE Evidence
            SET description = %s, id_type_evidence = %s
            WHERE id_evidence = %s;
            """,
            ("Updated description", 2, 1)
        )

    def test_delete_nonexistent_evidence(self):
        # Mock the database response
        self.evidence_controller.db.execute_query.return_value = None

        # Call the method
        self.evidence_controller.delete_evidence(999)

        # Assertions
        self.evidence_controller.db.execute_query.assert_called_with(
            "DELETE FROM Evidence WHERE id_evidence = %s;",
            (999,)
        )

    def test_update_evidence_invalid_id(self):
        # Mock the database response
        self.evidence_controller.db.execute_query.return_value = None

        # Call the method
        self.evidence_controller.update_evidence(999, description="Invalid ID")

        # Assertions
        self.evidence_controller.db.execute_query.assert_called_with(
            """
            UPDATE Evidence
            SET description = %s
            WHERE id_evidence = %s;
            """,
            ("Invalid ID", 999)
        )

    def test_update_evidence_no_fields(self):
        # Call the method
        self.evidence_controller.update_evidence(1)

        # Assertions
        self.evidence_controller.db.execute_query.assert_not_called()

if __name__ == "__main__":
    unittest.main()



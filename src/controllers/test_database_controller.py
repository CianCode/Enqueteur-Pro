import unittest
from unittest.mock import patch, MagicMock
from database_controller import DatabaseController
import psycopg2


class TestDatabaseController(unittest.TestCase):

    def setUp(self):
        self.db_controller = DatabaseController()

    @patch("psycopg2.connect")
    def test_connect_success(self, mock_connect):
        mock_connect.return_value.cursor.return_value = MagicMock()
        try:
            self.db_controller.connect()
            self.assertIsNotNone(self.db_controller.conn)
            self.assertIsNotNone(self.db_controller.cursor)
        finally:
            self.db_controller.close_connection()

    @patch("psycopg2.connect", side_effect=psycopg2.OperationalError("Connection failed"))
    def test_connect_operational_error(self, mock_connect):
        with self.assertRaises(psycopg2.OperationalError):
            self.db_controller.connect()

    @patch("psycopg2.connect")
    def test_execute_query_success(self, mock_connect):
        mock_connect.return_value.cursor.return_value = MagicMock()
        self.db_controller.connect()
        mock_execute = self.db_controller.cursor.execute
        self.db_controller.execute_query("SELECT 1;")
        mock_execute.assert_called_once_with("SELECT 1;", ())
        self.db_controller.close_connection()

    @patch("psycopg2.connect")
    def test_execute_query_programming_error(self, mock_connect):
        mock_connect.return_value.cursor.return_value = MagicMock()
        self.db_controller.connect()
        self.db_controller.cursor.execute.side_effect = psycopg2.ProgrammingError("Syntax error")
        with self.assertRaises(psycopg2.ProgrammingError):
            self.db_controller.execute_query("INVALID QUERY;")
        self.db_controller.close_connection()

    @patch("psycopg2.connect")
    def test_execute_query_integrity_error(self, mock_connect):
        mock_connect.return_value.cursor.return_value = MagicMock()
        self.db_controller.connect()
        self.db_controller.cursor.execute.side_effect = psycopg2.IntegrityError("Integrity constraint violation")
        with self.assertRaises(psycopg2.IntegrityError):
            self.db_controller.execute_query("INSERT INTO table VALUES (1);")
        self.db_controller.close_connection()

    @patch("psycopg2.connect")
    def test_get_version_success(self, mock_connect):
        mock_connect.return_value.cursor.return_value = MagicMock()
        self.db_controller.connect()
        mock_fetch = self.db_controller.cursor.fetchall
        mock_fetch.return_value = [("PostgreSQL 14.0")]
        version = self.db_controller.get_version()
        self.assertEqual(version, [("PostgreSQL 14.0")])
        self.db_controller.close_connection()


if __name__ == "__main__":
    unittest.main()

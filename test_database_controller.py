import unittest
from unittest.mock import patch, MagicMock
from src.controllers.database_controller import DatabaseController

class TestDatabaseController(unittest.TestCase):

    @patch("psycopg2.connect")
    def test_connect_success(self, mock_connect):
        """Test successful connection to the database."""
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        db = DatabaseController()
        db.connect()

        self.assertIsNotNone(db.conn)
        self.assertIsNotNone(db.cursor)
        mock_connect.assert_called_once()

    @patch("psycopg2.connect")
    def test_connect_failure(self, mock_connect):
        """Test connection failure with invalid credentials."""
        mock_connect.side_effect = Exception("Connection failed")

        db = DatabaseController()
        with self.assertRaises(Exception):
            db.connect()

        self.assertIsNone(db.conn)
        self.assertIsNone(db.cursor)

    @patch("psycopg2.connect")
    def test_execute_query_success(self, mock_connect):
        """Test executing a query successfully."""
        mock_cursor = MagicMock()
        mock_connection = MagicMock(cursor=MagicMock(return_value=mock_cursor))
        mock_connect.return_value = mock_connection

        db = DatabaseController()
        db.connect()
        mock_cursor.execute.return_value = None

        db.execute_query("SELECT * FROM test_table;")
        mock_cursor.execute.assert_called_once_with("SELECT * FROM test_table;", ())

    @patch("psycopg2.connect")
    def test_execute_query_fetch_results(self, mock_connect):
        """Test fetching query results."""
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("version",)]
        mock_connection = MagicMock(cursor=MagicMock(return_value=mock_cursor))
        mock_connect.return_value = mock_connection

        db = DatabaseController()
        db.connect()

        results = db.execute_query("SELECT version();", fetch_results=True)
        self.assertEqual(results, [("version",)])
        mock_cursor.execute.assert_called_once_with("SELECT version();", ())

    @patch("psycopg2.connect")
    def test_close_connection(self, mock_connect):
        """Test closing the database connection."""
        mock_cursor = MagicMock()
        mock_connection = MagicMock(cursor=MagicMock(return_value=mock_cursor))
        mock_connect.return_value = mock_connection

        db = DatabaseController()
        db.connect()
        db.close_connection()

        mock_cursor.close.assert_called_once()
        mock_connection.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()

import os
from dotenv import load_dotenv
import psycopg2


class DatabaseController:
    def __init__(self):
        """Initialize the DatabaseController and load environment variables."""
        load_dotenv()
        self.db_password = os.getenv("POSTGRES_PASSWORD")
        self.db_user = os.getenv("POSTGRES_USER")
        self.db_name = os.getenv("POSTGRES_DB")
        self.db_host = "127.0.0.1"  # Assuming the database is running locally
        self.db_port = "5432"  # Default PostgreSQL port

        self.conn = None
        self.cursor = None

    def connect(self):
        """Establish the connection to the database."""
        try:
            conn_string = f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
            self.conn = psycopg2.connect(conn_string)
            self.cursor = self.conn.cursor()
            print(f"Connected to database '{self.db_name}' as user '{self.db_user}'.")
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            self.conn = None
            raise

    def execute_query(self, query, params=None, fetch_results=False):
        """
        Execute a SQL query on the database.

        :param query: The SQL query to execute.
        :param params: Parameters for the query (default: None).
        :param fetch_results: Whether to fetch and return results (default: False).
        :return: Query results if fetch_results is True, otherwise None.
        """
        if not self.conn or not self.cursor:
            print("Database connection is not established.")
            return None

        try:
            self.cursor.execute(query, params or ())
            if fetch_results:
                return self.cursor.fetchall()
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            raise

    def close_connection(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Database connection closed.")

    def get_version(self):
        """
        Get the PostgreSQL server version.

        :return: The version of the PostgreSQL server.
        """
        query = "SELECT version();"
        return self.execute_query(query, fetch_results=True)

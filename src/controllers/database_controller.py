import os
from dotenv import load_dotenv
import psycopg2

class DatabaseController:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()

        # Fetch the environment variables
        self.db_password = os.getenv("POSTGRES_PASSWORD")
        self.db_user = os.getenv("POSTGRES_USER")
        self.db_name = os.getenv("POSTGRES_DB")
        self.db_host = "127.0.0.1"  # Assuming the database is running locally
        self.db_port = "5432"  # Default PostgreSQL port

        # Initialize the connection variable
        self.conn = None
        self.cursor = None

    def connect(self):
        """Establish the connection to the database."""
        try:
            conn_string = f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
            self.conn = psycopg2.connect(conn_string)
            self.cursor = self.conn.cursor()
            print(f"Successfully connected to the database '{self.db_name}' as '{self.db_user}'.")
        except Exception as e:
            print(f"Error while connecting to the database: {e}")
            self.conn = None  # Set to None if connection fails
            raise

    def execute_query(self, query, params=None, fetch_results=False):
        """Execute a query on the database."""
        if not self.conn or not self.cursor:
            print("Database connection or cursor is not established.")
            return None

        try:
            if params is None:
                params = ()

            self.cursor.execute(query, params)

            if fetch_results:
                results = self.cursor.fetchall()
                return results
            else:
                self.conn.commit()

        except Exception as e:
            print(f"Error while executing the query: {e}")
            self.conn.rollback()
            raise  # re-raise the exception so it can be caught elsewhere


        except Exception as e:
            print(f"Error while executing the query: {e}")
            self.conn.rollback()

    def close_connection(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("Database connection closed.")

    def get_version(self):
        """Get the PostgreSQL server version."""
        query = "SELECT version();"
        return self.execute_query(query, fetch_results=True)

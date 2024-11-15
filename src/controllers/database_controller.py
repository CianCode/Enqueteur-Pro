# database_controller.py

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
            # Construct the connection string
            conn_string = f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

            # Establish the connection
            self.conn = psycopg2.connect(conn_string)

            # Create a cursor object to interact with the database
            self.cursor = self.conn.cursor()
            print(f"Successfully connected to the database '{self.db_name}' as '{self.db_user}'.")

        except Exception as e:
            print(f"Error while connecting to the database: {e}")

    def execute_query(self, query, fetch_results=False):
        """Execute a query on the database."""
        try:
            # Execute the given query
            self.cursor.execute(query)

            if fetch_results:
                # Fetch all the results if needed
                results = self.cursor.fetchall()
                return results
            else:
                # Commit the transaction if no results are needed
                self.conn.commit()

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

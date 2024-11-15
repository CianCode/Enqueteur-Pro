import datetime
from src.controllers.database_controller import DatabaseController


class InvestigationController:
    def __init__(self):
        """Initialize the Investigation Controller."""
        self.db = DatabaseController()
        self.db.connect()

    def create_investigation(self, name, type_crime, status, date_open=None):
        """
        Create a new investigation.

        :param name: The name of the investigation.
        :param type_crime: The ID of the crime type (foreign key).
        :param status: The status of the investigation ('open', 'closed').
        :param date_open: The date the investigation was opened (optional, defaults to today).
        :return: None
        """
        if not date_open:
            date_open = datetime.date.today()

        query = f"""
        INSERT INTO Investigation (name, type_crime, status, date_open)
        VALUES ('{name}', {type_crime}, '{status}', '{date_open}')
        RETURNING id_investigation;
        """
        try:
            result = self.db.execute_query(query, fetch_results=True)
            print(f"Investigation created with ID: {result[0][0]}")
        except Exception as e:
            print(f"Error creating investigation: {e}")

    def get_investigation_by_id(self, investigation_id):
        """
        Retrieve an investigation by ID.

        :param investigation_id: The ID of the investigation to retrieve.
        :return: Investigation details or None if not found.
        """
        query = f"SELECT * FROM Investigation WHERE id_investigation = {investigation_id};"
        try:
            result = self.db.execute_query(query, fetch_results=True)
            if result:
                return result[0]
            print(f"No investigation found with ID: {investigation_id}")
            return None
        except Exception as e:
            print(f"Error retrieving investigation: {e}")
            return None

    def update_investigation(self, investigation_id, name=None, type_crime=None, status=None, date_close=None):
        """
        Update an investigation's details.

        :param investigation_id: The ID of the investigation to update.
        :param name: New name of the investigation (optional).
        :param type_crime: New type of crime ID (optional).
        :param status: New status ('open', 'closed') (optional).
        :param date_close: New closing date (optional).
        :return: None
        """
        updates = []
        if name:
            updates.append(f"name = '{name}'")
        if type_crime:
            updates.append(f"type_crime = {type_crime}")
        if status:
            updates.append(f"status = '{status}'")
        if date_close:
            updates.append(f"date_close = '{date_close}'")

        if updates:
            query = f"""
            UPDATE Investigation
            SET {', '.join(updates)}
            WHERE id_investigation = {investigation_id};
            """
            try:
                self.db.execute_query(query)
                print(f"Investigation {investigation_id} updated successfully.")
            except Exception as e:
                print(f"Error updating investigation: {e}")

    def delete_investigation(self, investigation_id):
        """
        Delete an investigation by ID.

        :param investigation_id: The ID of the investigation to delete.
        :return: None
        """
        query = f"DELETE FROM Investigation WHERE id_investigation = {investigation_id};"
        try:
            self.db.execute_query(query)
            print(f"Investigation {investigation_id} deleted successfully.")
        except Exception as e:
            print(f"Error deleting investigation: {e}")

    def list_investigations(self):
        """
        Retrieve a list of all investigations.

        :return: A list of all investigations.
        """
        query = "SELECT * FROM investigation"
        try:
            result = self.db.execute_query(query, fetch_results=True)
            return result
        except Exception as e:
            print(f"Error listing investigations: {e}")
            return []

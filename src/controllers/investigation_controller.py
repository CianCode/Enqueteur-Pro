from src.controllers.database_controller import DatabaseController
from psycopg2 import sql

class InvestigationController:
    def __init__(self):
        self.db = DatabaseController()
        self.db.connect()  # Ensure connection is established before any DB operation
        if self.db.conn is None:
            print("Failed to establish database connection.")
            return

    def add_investigation(self, name, type_crime_id, status, date_open, date_close=None):
        """
        Add a new investigation to the database.

        :param name: Name of the investigation.
        :param type_crime_id: ID of the crime type.
        :param status: Status of the investigation ('open' or 'closed').
        :param date_open: Opening date of the investigation.
        :param date_close: Closing date of the investigation (optional).
        :return: ID of the inserted investigation if successful, None otherwise.
        """
        query = """
        INSERT INTO Investigation (name, type_crime, status, date_open, date_close)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_investigation;
        """
        params = (name, type_crime_id, status, date_open, date_close)
        result = self.db.execute_query(query, params)
        return result[0][0] if result else None

    def delete_investigation(self, investigation_id):
        """Delete an investigation by its ID."""
        query = "DELETE FROM Investigation WHERE id_investigation = %s;"
        params = (investigation_id,)
        self.db.execute_query(query, params)

    def list_investigations(self):
        """List all investigations in the database."""
        query = "SELECT * FROM Investigation;"
        result = self.db.execute_query(query, fetch_results=True)
        return result

    def update_investigation(self, investigation_id, name=None, type_crime_id=None, status=None, date_open=None, date_close=None):
        """Update an investigation's details."""
        set_clause = []
        params = []

        if name:
            set_clause.append("name = %s")
            params.append(name)
        if type_crime_id:
            set_clause.append("type_crime = %s")
            params.append(type_crime_id)
        if status:
            set_clause.append("status = %s")
            params.append(status)
        if date_open:
            set_clause.append("date_open = %s")
            params.append(date_open)
        if date_close:
            set_clause.append("date_close = %s")
            params.append(date_close)

        # If there are fields to update
        if set_clause:
            query = sql.SQL("UPDATE Investigation SET {} WHERE id_investigation = %s;").format(
                sql.SQL(", ").join(map(sql.Identifier, set_clause))
            )
            params.append(investigation_id)
            self.db.execute_query(query, tuple(params))

    def get_investigation_by_id(self, investigation_id):
        """Get an investigation by its ID."""
        query = "SELECT * FROM Investigation WHERE id_investigation = %s;"
        params = (investigation_id,)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result[0] if result else None

    def list_investigation_for_reports(self, investigation_id):
        """List all reports for a given investigation."""
        query = "SELECT * FROM Report WHERE investigation_relation = %s;"
        params = (investigation_id,)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result

    def list_investigation_for_people(self, investigation_id):
        """List all people related to a given investigation (suspects, witnesses)."""
        query = """
        SELECT p.first_name, p.last_name, tp.label AS person_type
        FROM Person p
        JOIN TypePersonne tp ON p.type_personne = tp.id
        JOIN Report r ON r.investigation_relation = p.id_personne
        WHERE r.investigation_relation = %s;
        """
        params = (investigation_id,)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result

    def list_investigation_for_evidences(self, investigation_id):
        """List all evidences related to a given investigation."""
        query = """
        SELECT e.id_evidence, e.description, te.label AS evidence_type
        FROM Evidence e
        JOIN TypeEvidence te ON e.id_type_evidence = te.id_type_evidence
        WHERE e.id_evidence IN (SELECT id_evidence FROM Report WHERE investigation_relation = %s);
        """
        params = (investigation_id,)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result

    def get_crime_type_label(self, type_crime_id):
        """Fetch the label of a crime type from the database by its ID."""
        query = "SELECT label FROM TypeCrime WHERE id_crime = %s;"
        params = (type_crime_id,)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result[0][0] if result else None


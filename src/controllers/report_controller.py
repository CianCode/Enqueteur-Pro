from src.controllers.database_controller import DatabaseController

class ReportController:
    def __init__(self):
        self.db = DatabaseController()

    def add_report(self, investigation_id, content):
        """Add a report for an investigation."""
        query = """
        INSERT INTO Report (date_creation, content, investigation_relation)
        VALUES (CURRENT_DATE, %s, %s) RETURNING id_report;
        """
        params = (content, investigation_id)
        result = self.db.execute_query(query, params)
        return result[0][0] if result else None

    def delete_report(self, report_id):
        """Delete a report by its ID."""
        query = "DELETE FROM Report WHERE id_report = %s;"
        params = (report_id,)
        self.db.execute_query(query, params)

    def list_reports_for_investigation(self, investigation_id):
        """List all reports for a given investigation."""
        query = "SELECT * FROM Report WHERE investigation_relation = %s;"
        params = (investigation_id,)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result

    def update_report(self, report_id, content):
        """Update the content of a report."""
        query = "UPDATE Report SET content = %s WHERE id_report = %s;"
        params = (content, report_id)
        self.db.execute_query(query, params)

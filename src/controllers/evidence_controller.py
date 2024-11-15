from src.controllers.database_controller import DatabaseController

class EvidenceController:
    def __init__(self):
        self.db = DatabaseController()

    def add_evidence(self, type_evidence_id, description):
        """Add evidence to the database."""
        query = """
        INSERT INTO Evidence (id_type_evidence, description)
        VALUES (%s, %s) RETURNING id_evidence;
        """
        params = (type_evidence_id, description)
        result = self.db.execute_query(query, params)
        return result[0][0] if result else None

    def delete_evidence(self, evidence_id):
        """Delete an evidence by its ID."""
        query = "DELETE FROM Evidence WHERE id_evidence = %s;"
        params = (evidence_id,)
        self.db.execute_query(query, params)

    def list_evidences_for_investigation(self, investigation_id):
        """List all evidences for a given investigation."""
        query = """
        SELECT e.id_evidence, e.description, te.label AS evidence_type
        FROM Evidence e
        JOIN TypeEvidence te ON e.id_type_evidence = te.id_type_evidence
        WHERE e.id_evidence IN (SELECT id_evidence FROM Report WHERE investigation_relation = %s);
        """
        params = (investigation_id,)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result

    def update_evidence(self, evidence_id, description=None, type_evidence_id=None):
        """Update a piece of evidence."""
        set_clause = []
        params = []

        if description:
            set_clause.append("description = %s")
            params.append(description)
        if type_evidence_id:
            set_clause.append("id_type_evidence = %s")
            params.append(type_evidence_id)

        if set_clause:
            query = f"""
            UPDATE Evidence
            SET {', '.join(set_clause)}
            WHERE id_evidence = %s;
            """
            params.append(evidence_id)
            self.db.execute_query(query, tuple(params))

from src.controllers.database_controller import DatabaseController

class PersonneController:
    def __init__(self):
        self.db = DatabaseController()

    def add_person(self, first_name, last_name, description, alibi, type_personne_id):
        """Add a person (suspect, witness) to the database."""
        query = """
        INSERT INTO Person (first_name, last_name, description, alibi, type_personne)
        VALUES (%s, %s, %s, %s, %s) RETURNING id_personne;
        """
        params = (first_name, last_name, description, alibi, type_personne_id)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result[0][0] if result else None

    def get_person_by_id(self, person_id):
        """Get a person by their ID."""
        query = "SELECT * FROM Person WHERE id_personne = %s;"
        params = (person_id,)
        result = self.db.execute_query(query, params, fetch_results=True)
        return result[0] if result else None

    def delete_person(self, person_id):
        """Delete a person by their ID."""
        query = "DELETE FROM Person WHERE id_personne = %s;"
        params = (person_id,)
        self.db.execute_query(query, params)

    def list_people_for_investigation(self, investigation_id):
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

    def update_person(self, person_id, first_name=None, last_name=None, description=None, alibi=None, type_personne_id=None):
        """Update a person's details."""
        set_clause = []
        params = []

        if first_name:
            set_clause.append("first_name = %s")
            params.append(first_name)
        if last_name:
            set_clause.append("last_name = %s")
            params.append(last_name)
        if description:
            set_clause.append("description = %s")
            params.append(description)
        if alibi:
            set_clause.append("alibi = %s")
            params.append(alibi)
        if type_personne_id:
            set_clause.append("type_personne = %s")
            params.append(type_personne_id)

        if set_clause:
            query = "UPDATE Person SET {} WHERE id_personne = %s;".format(", ".join(set_clause))
            params.append(person_id)
            self.db.execute_query(query, tuple(params))

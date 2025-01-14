from datetime import date
from controllers.investigation_controller import InvestigationController

#function that add an investigations

def add_investigation(name, type_crime_id, status, date_open, date_close=None):
    investigation_controller = InvestigationController()
    return investigation_controller.add_investigation(name, type_crime_id, status, date_open, date_close)

add_investigation("Exam", 1, "open", date(2021, 1, 1))

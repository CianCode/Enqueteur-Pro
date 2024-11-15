from datetime import date
from controllers.investigation_controller import InvestigationController

#function that lists all investigations
def list_investigations():
    controller = InvestigationController()
    investigations = controller.list_investigations()
    if investigations:
        for investigation in investigations:
            print(investigation)
    else:
        print("No investigations found.")

list_investigations()

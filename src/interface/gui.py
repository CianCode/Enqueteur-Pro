import tkinter as tk
from interface.frames import Navbar, EnqueteFrame, InvestigationDetailsFrame, PersonneFrame, RapportFrame  # Correct module import


class DatabaseApp:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Database Application")
        self.root.geometry("800x600")
        self.root.configure(bg="#ECF0F1")
        self.controller = controller  # Pass the controller to the app

        # Navbar
        self.navbar = Navbar(self.root, self.show_enquete, self.show_personne, self.show_rapport)

        # Content frame
        self.content = tk.Frame(self.root, bg="#ECF0F1")
        self.content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Frames
        self.details_frame = InvestigationDetailsFrame(self.content)
        self.enquete_frame = EnqueteFrame(self.content, self.show_investigation_details, self.controller)
        self.personne_frame = PersonneFrame(self.content)
        self.rapport_frame = RapportFrame(self.content)

        # Place frames
        self.details_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.enquete_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.personne_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.rapport_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Default frame
        self.show_enquete()

    def show_enquete(self):
        self.personne_frame.lower()
        self.rapport_frame.lower()
        self.details_frame.lower()
        self.enquete_frame.lift()

    def show_personne(self):
        self.enquete_frame.lower()
        self.rapport_frame.lower()
        self.details_frame.lower()
        self.personne_frame.lift()

    def show_rapport(self):
        self.enquete_frame.lower()
        self.personne_frame.lower()
        self.details_frame.lower()
        self.rapport_frame.lift()

    def show_investigation_details(self, investigation):
        self.enquete_frame.lower()
        self.details_frame.lift()
        self.details_frame.update_details(investigation)
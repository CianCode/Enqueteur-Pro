import tkinter as tk
from interface.frames import Navbar, EnqueteFrame, PersonneFrame, RapportFrame, EvidenceFrame  # Correct module import


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Application")
        self.root.geometry("800x600")
        self.root.configure(bg="#ECF0F1")  # Set background for the main window

        # Create a container for the navigation bar and content
        self.navbar = Navbar(self.root, self.show_enquete, self.show_personne, self.show_rapport, self.show_evidences)

        # Create a container for the content
        self.content = tk.Frame(self.root, bg="#ECF0F1")
        self.content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Initialize frames
        self.frame1 = EnqueteFrame(self.content)
        self.frame2 = PersonneFrame(self.content)
        self.frame3 = RapportFrame(self.content)
        self.frame4 = EvidenceFrame(self.content)

        # Place both frames in the same location
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame2.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame3.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame4.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Show the first frame by default
        self.show_enquete()

    def show_enquete(self):
        self.frame2.lower()  # Send frame2 to the back
        self.frame3.lower()  # Send frame3 to the back
        self.frame4.lower()
        self.frame1.lift()  # Bring frame1 to the front

    def show_personne(self):
        self.frame1.lower()  # Send frame1 to the back
        self.frame3.lower()  # Send frame3 to the back
        self.frame4.lower()
        self.frame2.lift()  # Bring frame2 to the front

    def show_rapport(self):
        self.frame1.lower()  # Send frame1 to the back
        self.frame2.lower()  # Send frame2 to the back
        self.frame4.lower()
        self.frame3.lift()  # Bring frame3 to the front

    def show_evidences(self):
        self.frame1.lower()
        self.frame2.lower()
        self.frame3.lower()
        self.frame4.lift()
import tkinter as tk
from tkinter import ttk


class Navbar(tk.Frame):
    def __init__(self, parent, show_enquete, show_personne, show_rapport, show_evidences):
        super().__init__(parent, bg="#F7F9F9", width=200)
        self.pack_propagate(False)

        # Icône en haut
        self.icon = tk.Label(self, text="◆", font=("Helvetica", 24), bg="#F7F9F9", fg="#34495E")
        self.icon.pack(pady=20)

        # Boutons de navigation
        self.enquete_button = tk.Button(self, text="Enquêtes", font=("Helvetica", 14), bg="#F7F9F9", fg="#2C3E50", bd=0,
                                        command=show_enquete)
        self.enquete_button.pack(pady=10, anchor="w", padx=20)

        self.personne_button = tk.Button(self, text="Personnes", font=("Helvetica", 14), bg="#F7F9F9", fg="#2C3E50", bd=0,
                                         command=show_personne)
        self.personne_button.pack(pady=10, anchor="w", padx=20)

        self.rapport_button = tk.Button(self, text="Rapports", font=("Helvetica", 14), bg="#F7F9F9", fg="#2C3E50", bd=0,
                                        command=show_rapport)
        self.rapport_button.pack(pady=10, anchor="w", padx=20)

        self.evidence_button = tk.Button(self, text="Évidences", font=("Helvetica", 14), bg="#F7F9F9", fg="#2C3E50", bd=0,
                                         command=show_evidences)
        self.evidence_button.pack(pady=10, anchor="w", padx=20)

        # Espace utilisateur en bas
        self.user_frame = tk.Frame(self, bg="#F7F9F9")
        self.user_frame.pack(side="bottom", pady=20)

        self.user_icon = tk.Label(self.user_frame, text="◯", font=("Helvetica", 20), bg="#F7F9F9", fg="#34495E")
        self.user_icon.pack()

        self.user_label = tk.Label(self.user_frame, text="USER", font=("Helvetica", 12), bg="#F7F9F9", fg="#2C3E50")
        self.user_label.pack()


class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Application")
        self.root.geometry("900x600")
        self.root.configure(bg="#ECF0F1")

        # Configuration du style général
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Helvetica", 12), background="#3498DB", foreground="white")
        self.style.map("TButton", background=[("active", "#2980B9")])

        # Barre de navigation
        self.navbar = Navbar(
            self.root,
            self.show_enquete,
            self.show_personne,
            self.show_rapport,
            self.show_evidences
        )
        self.navbar.pack(side="left", fill="y")

        # Conteneur principal pour les frames
        self.content = tk.Frame(self.root, bg="#ECF0F1")
        self.content.pack(side="right", fill="both", expand=True)

        # Initialisation des frames
        self.frames = {
            "enquete": self.create_empty_frame("Enquêtes"),
            "personne": self.create_empty_frame("Personnes"),
            "rapport": self.create_empty_frame("Rapports"),
            "evidences": self.create_empty_frame("Évidences"),
        }

        # Positionnement de chaque frame
        for frame in self.frames.values():
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Afficher la frame par défaut avec "Bienvenue"
        self.show_welcome_message()

    def create_empty_frame(self, title):
        """Créer un frame vide avec un titre temporaire."""
        frame = tk.Frame(self.content, bg="#ECF0F1")
        label = tk.Label(frame, text=title, font=("Helvetica", 18, "bold"), bg="#ECF0F1", fg="#2C3E50")
        label.pack(expand=True)
        return frame

    def show_frame(self, frame_name):
        """Affiche la frame correspondante au nom donné."""
        for name, frame in self.frames.items():
            if name == frame_name:
                frame.lift()
            else:
                frame.lower()

    def show_welcome_message(self):
        """Affiche un message de bienvenue au démarrage."""
        welcome_frame = tk.Frame(self.content, bg="#ECF0F1")
        welcome_label = tk.Label(welcome_frame, text="Bienvenue", font=("Helvetica", 24, "bold"), bg="#ECF0F1", fg="#2C3E50")
        welcome_label.pack(expand=True)
        welcome_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.current_frame = welcome_frame

    def show_enquete(self):
        self.show_frame("enquete")

    def show_personne(self):
        self.show_frame("personne")

    def show_rapport(self):
        self.show_frame("rapport")

    def show_evidences(self):
        self.show_frame("evidences")


if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

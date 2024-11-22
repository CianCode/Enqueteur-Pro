import tkinter as tk
from tkinter import ttk


class Navbar(tk.Frame):
    def __init__(self, parent, show_enquete, show_personne, show_rapport, show_evidences):
        super().__init__(parent, bg="#2C3E50")
        self.show_enquete = show_enquete
        self.show_personne = show_personne
        self.show_rapport = show_rapport
        self.show_evidences = show_evidences

        # Boutons de navigation
        ttk.Button(self, text="Enquêtes", command=self.show_enquete).pack(fill="x", pady=2, padx=5)
        ttk.Button(self, text="Personnes", command=self.show_personne).pack(fill="x", pady=2, padx=5)
        ttk.Button(self, text="Rapports", command=self.show_rapport).pack(fill="x", pady=2, padx=5)
        ttk.Button(self, text="Évidences", command=self.show_evidences).pack(fill="x", pady=2, padx=5)

        # Bouton utilisateur (simulé en bas de la navbar)
        user_button = tk.Button(self, text="USER", bg="#34495E", fg="white", relief="flat", font=("Helvetica", 12, "bold"))
        user_button.pack(side="bottom", fill="x", pady=10)


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
            self.show_evidences,
        )
        self.navbar.pack(side="left", fill="y")

        # Conteneur principal pour les frames
        self.content = tk.Frame(self.root, bg="#ECF0F1")
        self.content.pack(side="right", fill="both", expand=True)

        # Initialisation des frames
        self.frames = {
            "enquete": self.create_investigation_frame(),
            "personne": self.create_empty_frame("Personnes"),
            "rapport": self.create_empty_frame("Rapports"),
            "evidences": self.create_empty_frame("Évidences"),
        }

        # Positionnement de chaque frame
        for frame in self.frames.values():
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Afficher la frame par défaut avec "Bienvenue"
        self.show_frame("enquete")  # Par défaut, on montre les enquêtes

    def create_empty_frame(self, title):
        """Créer un frame vide avec un titre temporaire."""
        frame = tk.Frame(self.content, bg="#ECF0F1")
        label = tk.Label(
            frame, text=title, font=("Helvetica", 18, "bold"), bg="#ECF0F1", fg="#2C3E50", anchor="w"
        )
        label.pack(anchor="nw", padx=10, pady=10)  # Placer en haut à gauche avec des marges
        return frame

    def show_frame(self, frame_name):
        """Affiche la frame correspondante au nom donné."""
        for name, frame in self.frames.items():
            if name == frame_name:
                frame.lift()
            else:
                frame.lower()

    def show_enquete(self):
        self.show_frame("enquete")

    def show_personne(self):
        self.show_frame("personne")

    def show_rapport(self):
        self.show_frame("rapport")

    def show_evidences(self):
        self.show_frame("evidences")

    def create_investigation_frame(self):
        """Créer une frame pour afficher les enquêtes avec un tableau."""
        frame = tk.Frame(self.content, bg="#ECF0F1")

        # Titre de la section
        title_label = tk.Label(
            frame,
            text="Liste des Enquêtes",
            font=("Helvetica", 16, "bold"),
            bg="#ECF0F1",
            fg="#2C3E50",
            anchor="w",
        )
        title_label.pack(fill="x", padx=10, pady=5)

        # Création du tableau (Treeview)
        columns = ("nom", "type", "statut", "date_ouverture")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        tree.heading("nom", text="Nom")
        tree.heading("type", text="Type")
        tree.heading("statut", text="Statut")
        tree.heading("date_ouverture", text="Date Ouverture")
        tree.column("nom", width=150, anchor="center")
        tree.column("type", width=100, anchor="center")
        tree.column("statut", width=100, anchor="center")
        tree.column("date_ouverture", width=120, anchor="center")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Bouton pour charger les données
        load_button = ttk.Button(
            frame,
            text="Charger les données",
            command=lambda: self.load_investigations(tree),
        )
        load_button.pack(pady=5)

        return frame

    def load_investigations(self, tree):
        """Charger les données des enquêtes dans le tableau."""
        # Exemple de récupération des données depuis la base (adapter avec votre méthode)
        data = [
            ("Enquête 1", "Criminel", "Ouverte", "2024-11-01"),
            ("Enquête 2", "Civil", "Fermée", "2024-10-15"),
            ("Enquête 3", "Financier", "En cours", "2024-11-10"),
        ]
        # Supprimer les anciennes données
        for item in tree.get_children():
            tree.delete(item)
        # Ajouter les nouvelles données
        for row in data:
            tree.insert("", "end", values=row)


# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

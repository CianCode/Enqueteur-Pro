import tkinter as tk
from tkinter import ttk, messagebox

from src.controllers.investigation_controller import InvestigationController


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
        self.investigation_name_label = None
        self.detail_title_label = None
        self.root = root
        self.root.title("Database Application")
        self.root.geometry("900x600")
        self.root.configure(bg="#ECF0F1")

        self.controller = InvestigationController()

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
            "detail": self.create_detail_frame(),
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
        columns = ("id", "nom", "type", "statut", "date_ouverture")
        tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        tree.heading("id", text="ID")
        tree.heading("nom", text="Nom")
        tree.heading("type", text="Type")
        tree.heading("statut", text="Statut")
        tree.heading("date_ouverture", text="Date Ouverture")
        tree.column("id", width=50, anchor="center")
        tree.column("nom", width=150, anchor="center")
        tree.column("type", width=100, anchor="center")
        tree.column("statut", width=100, anchor="center")
        tree.column("date_ouverture", width=120, anchor="center")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Bind double-click event to the treeview
        tree.bind("<Double-1>", lambda event: self.on_investigation_click(event, tree))

        self.load_investigations(tree)  # Charger les données dans le tableau

        return frame

    def load_investigations(self, tree):
        """Charger les données des enquêtes dans le tableau depuis la base de données."""
        try:
            # Récupérer les données depuis la base
            data = self.controller.list_investigations()  # Appeler la méthode pour récupérer les données
            # Supprimer les anciennes données dans le tableau
            for item in tree.get_children():
                tree.delete(item)
            # Ajouter les nouvelles données
            for row in data:
                tree.insert("", "end", values=row)
        except Exception as e:
            # Gérer les erreurs si la base n'est pas connectée
            print(f"Erreur lors du chargement des données : {e}")

    def create_detail_frame(self):
        """Créer une frame pour afficher les détails d'une enquête."""
        frame = tk.Frame(self.content, bg="#ECF0F1")

        # Label pour le titre de l'enquête
        self.detail_title_label = tk.Label(
            frame, text="Détails de l'enquête", font=("Helvetica", 18, "bold"), bg="#ECF0F1", fg="#2C3E50"
        )
        self.detail_title_label.pack(pady=20)

        # Label pour afficher le nom de l'enquête
        self.investigation_name_label = tk.Label(
            frame, text="", font=("Helvetica", 14), bg="#ECF0F1", fg="#34495E"
        )
        self.investigation_name_label.pack(pady=10)

        return frame


    def on_investigation_click(self, event, tree):
        """Handle clicking on an investigation to display details."""
        selected_item = tree.selection()
        if selected_item:
            # Retrieve the selected row's data
            item_data = tree.item(selected_item[0])["values"]
            if item_data:
                investigation_id = item_data[0]  # Assuming the first column is the ID
                investigation_name = item_data[1]  # Assuming the second column is the name

                # Display details in the "detail" frame
                self.detail_title_label.config(text=f"Détails de l'enquête : {investigation_name}")
                self.investigation_name_label.config(text=f"Nom de l'enquête : {investigation_name}")
                self.show_frame("detail")
        else:
            messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une enquête.")
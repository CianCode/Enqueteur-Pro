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
        self.investigation_status_label = None
        self.investigation_type_label = None
        self.investigation_date_label = None
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
                type_crime_id = row[2]  # Assuming the crime type ID is at index 2
                type_crime_label = self.controller.get_crime_type_label(type_crime_id)
                row_with_label = list(row)  # Convert tuple to list to modify it
                row_with_label[2] = type_crime_label  # Replace the crime type ID with its label
                tree.insert("", "end", values=row_with_label)  # Insert row with the crime type label
        except Exception as e:
            # Gérer les erreurs si la base n'est pas connectée
            print(f"Erreur lors du chargement des données : {e}")

    def create_horizontal_sub_container(self, parent, title, investigation_id):
        """Create a horizontal sub-container with a title and a list of people or evidence."""
        # Frame for each container
        container = tk.Frame(parent, bg="#E8F6F3", bd=2, relief="groove")
        container.pack(side="left", expand=True, fill="both", padx=5, pady=5)

        # Title of the container (without inside the container)
        container_title = tk.Label(
            container,
            text=title,
            font=("Helvetica", 14, "bold"),
            bg="#E8F6F3",
            fg="#2C3E50",
            anchor="center",
        )
        container_title.pack(fill="x", padx=5, pady=5)

        # Depending on the title, we show either people or evidence in the container
        if title == "Personnes":
            self.populate_people_list(container, investigation_id)
        elif title == "Évidences":
            self.populate_evidence_list(container, investigation_id)

    def populate_people_list(self, container, investigation_id):
        """Populate the container with a list of people related to the investigation."""
        # Get the data for people related to the investigation
        people_data = self.controller.list_investigation_for_people(investigation_id)

        # Create the Listbox for people
        listbox = tk.Listbox(container, font=("Helvetica", 12), bg="#E8F6F3", fg="#2C3E50")
        listbox.pack(fill="both", expand=True, padx=5, pady=10)

        # Insert the data into the Listbox
        for person in people_data:
            full_name = f"{person['first_name']} {person['last_name']}"  # Full name
            person_type = person['person_type']  # Person type (suspect, witness, etc.)
            listbox.insert(tk.END, f"{full_name} - {person_type}")

    def populate_evidence_list(self, container, investigation_id):
        """Populate the container with a list of evidence related to the investigation."""
        # Get the data for evidence related to the investigation
        evidence_data = self.controller.list_investigation_for_evidences(investigation_id)

        # Create the Listbox for evidence
        listbox = tk.Listbox(container, font=("Helvetica", 12), bg="#E8F6F3", fg="#2C3E50")
        listbox.pack(fill="both", expand=True, padx=5, pady=10)

        # Insert the data into the Listbox
        for evidence in evidence_data:
            evidence_description = evidence['description']  # Description
            evidence_type = evidence['evidence_type']  # Evidence type
            listbox.insert(tk.END, f"{evidence_description} - {evidence_type}")

    def create_detail_frame(self):
        """Créer une frame pour afficher les détails d'une enquête sélectionnée, avec trois conteneurs alignés horizontalement."""
        frame = tk.Frame(self.content, bg="#ECF0F1")

        # Titre principal de la section
        self.detail_title_label = tk.Label(
            frame,
            text="Détails de l'enquête",
            font=("Helvetica", 18, "bold"),
            bg="#ECF0F1",
            fg="#2C3E50",
            anchor="w",
        )
        self.detail_title_label.pack(fill="x", padx=10, pady=10)

        # Conteneur principal pour les détails de l'enquête
        details_container = tk.Frame(frame, bg="#D5DBDB", bd=2, relief="groove")
        details_container.pack(fill="x", padx=20, pady=10)

        # Labels pour les informations détaillées dans le conteneur principal
        self.investigation_name_label = tk.Label(
            details_container,
            text="Nom de l'enquête :",
            font=("Helvetica", 14),
            bg="#D5DBDB",
            fg="#2C3E50",
            anchor="w",
        )
        self.investigation_name_label.pack(fill="x", padx=10, pady=5)

        self.investigation_type_label = tk.Label(
            details_container,
            text="Type de l'enquête :",
            font=("Helvetica", 14),
            bg="#D5DBDB",
            fg="#2C3E50",
            anchor="w",
        )
        self.investigation_type_label.pack(fill="x", padx=10, pady=5)

        self.investigation_status_label = tk.Label(
            details_container,
            text="Statut de l'enquête :",
            font=("Helvetica", 14),
            bg="#D5DBDB",
            fg="#2C3E50",
            anchor="w",
        )
        self.investigation_status_label.pack(fill="x", padx=10, pady=5)

        self.investigation_date_label = tk.Label(
            details_container,
            text="Date d'ouverture :",
            font=("Helvetica", 14),
            bg="#D5DBDB",
            fg="#2C3E50",
            anchor="w",
        )
        self.investigation_date_label.pack(fill="x", padx=10, pady=5)

        # Conteneur horizontal pour les trois sous-sections
        horizontal_container = tk.Frame(frame, bg="#ECF0F1")
        horizontal_container.pack(fill="x", padx=20, pady=10)

        # Création des trois conteneurs horizontaux
        investigation_id = 1  # Replace with the actual investigation ID
        self.create_horizontal_sub_container(horizontal_container, "Personnes", investigation_id)
        self.create_horizontal_sub_container(horizontal_container, "Évidences", investigation_id)

        # Placeholder for the third container
        self.create_horizontal_sub_container(horizontal_container, "Autre Information", investigation_id)

        # Bouton de retour
        back_button = ttk.Button(
            frame,
            text="Retour",
            command=lambda: self.show_frame("enquete"),
        )
        back_button.pack(pady=10)

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
                investigation_type = item_data[2]  # Assuming the third column is the type (now label)
                investigation_status = item_data[3]  # Assuming the fourth column is the status
                investigation_date = item_data[4]  # Assuming the fifth column is the date

                # Update the labels in the detail frame
                self.detail_title_label.config(text=f"Détails de l'enquête : {investigation_name}")
                self.investigation_name_label.config(text=f"Nom de l'enquête : {investigation_name}")
                self.investigation_type_label.config(text=f"Type de l'enquête : {investigation_type}")
                self.investigation_status_label.config(text=f"Statut de l'enquête : {investigation_status}")
                self.investigation_date_label.config(text=f"Date d'ouverture : {investigation_date}")

                # Show the detail frame
                self.show_frame("detail")
        else:
            messagebox.showwarning("Aucune sélection", "Veuillez sélectionner une enquête.")
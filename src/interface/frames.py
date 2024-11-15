import tkinter as tk

class Navbar(tk.Frame):
    def __init__(self, parent, show_content1_callback, show_content2_callback, show_content3_callback):
        super().__init__(parent, bg="#34495E", width=100)  # Dark blue background for navbar
        self.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        self.nav_title = tk.Label(self, text="Navigation", font=("Arial", 16), bg="#34495E", fg="white")
        self.nav_title.pack(pady=10, padx=5, fill=tk.X)

        # Buttons for navigation, accepting callback functions for content switching
        self.nav_button1 = tk.Button(self, text="Enquete", command=show_content1_callback , fg="black", font=("Arial", 12), relief="flat", width=15, height=2)
        self.nav_button1.pack(pady=10, padx=5, fill=tk.X)

        self.nav_button2 = tk.Button(self, text="Personne", command=show_content2_callback , fg="black", font=("Arial", 12), relief="flat", width=15, height=2)
        self.nav_button2.pack(pady=10, padx=5, fill=tk.X)

        self.nav_button3 = tk.Button(self, text="Rapport", command=show_content3_callback, fg="black", font=("Arial", 12), relief="flat", width=15, height=2)
        self.nav_button3.pack(pady=10, padx=5, fill=tk.X)


class EnqueteFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")  # Light gray background for content frame
        label = tk.Label(self, text="Enquete", font=("Arial", 20, "bold"), bg="#ECF0F1", fg="#34495E")  # Dark text for contrast
        label.pack(pady=20)


class PersonneFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")  # Light gray background for content frame
        label = tk.Label(self, text="Personne Fichier", font=("Arial", 20, "bold"), bg="#ECF0F1", fg="#34495E")  # Dark text for contrast
        label.pack(pady=20)


class RapportFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")  # Light gray background for content frame
        label = tk.Label(self, text="Rapport d'Enquete", font=("Arial", 20, "bold"), bg="#ECF0F1", fg="#34495E")  # Dark text for contrast
        label.pack(pady=20)

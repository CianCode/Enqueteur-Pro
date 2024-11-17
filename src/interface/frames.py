import tkinter as tk
from tkinter import ttk

class NavRoundedButton(ttk.Button):
    def __init__(self, parent, text, command=None, **kwargs):
        # Use the 'alt' theme to bypass native Aqua theme
        style = ttk.Style()
        style.theme_use('alt')  # Switch to a customizable theme
        style.configure(
            "Rounded.TButton",
            font=("Arial", 12),
            padding=8,
            relief="flat",
            background="#11181f",  # Default button color
            foreground="white",
            borderwidth=0,
            width=20,

        )
        style.map(
            "Rounded.TButton",
            background=[("active", "#6b9ac9"), ("pressed", "darkblue")],
            foreground=[("disabled", "gray")]
        )
        super().__init__(parent, text=text, command=command, style="Rounded.TButton", **kwargs)

class Navbar(tk.Frame):
    def __init__(self, parent, show_content1_callback, show_content2_callback, show_content3_callback, show_content4_callback):
        super().__init__(parent, bg="#34495E", width=100)  # Dark blue background for navbar
        self.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        self.nav_title = tk.Label(self, text="Navigation", font=("Arial", 16), bg="#34495E", fg="white")
        self.nav_title.pack(pady=10, padx=5, fill=tk.X)

        # Buttons for navigation, accepting callback functions for content switching
        self.nav_button1 = NavRoundedButton(self, text="Enquete", command=show_content1_callback)
        self.nav_button1.pack(pady=15, padx=15, fill=tk.X)

        self.nav_button2 = NavRoundedButton(self, text="Personne", command=show_content2_callback)
        self.nav_button2.pack(pady=15, padx=15, fill=tk.X)

        self.nav_button3 = NavRoundedButton(self, text="Rapport", command=show_content3_callback, width=20)
        self.nav_button3.pack(pady=15, padx=15, fill=tk.X)

        self.nav_button4 = NavRoundedButton(self, text="Evidences", command=show_content4_callback, width=20)
        self.nav_button4.pack(pady=15, padx=15, fill=tk.X)


class EnqueteFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")  # Light gray background for content frame
        label = tk.Label(self, text="Select an Investigation", font=("Arial", 20, "bold"), bg="#ECF0F1", fg="#34495E")  # Dark text for contrast
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

class EvidenceFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")  # Light gray background for content frame
        label = tk.Label(self, text="Evidence", font=("Arial", 20, "bold"), bg="#ECF0F1", fg="#34495E")  # Dark text for contrast
        label.pack(pady=20)
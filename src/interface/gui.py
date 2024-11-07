# Description : Contains the main frame of the GUI

# Importing the necessary libraries
import tkinter as tk

# ? Defining the function on_button_click
def on_button_click():
    """ * Placeholder method for the button click event """
    print("Le bouton a été cliqué!")

# ? Defining the class EnqueteurProApp
class EnqueteurProApp:
    """ * A class that represents the window available to the user. It contains frames and can replace them to display different views """

    def __init__(self, root):
        self.root = root
        self.root.title("Enqueteur Pro - Gestionnaire d'enquêtes")
        self.root.configure(background="white")

        # * Set window size
        self.root.geometry("800x600")

        # * Add a frame for content
        self.frame = tk.Frame(self.root, bg="white")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # * Add a label to display some text
        self.label = tk.Label(self.frame, text="Bienvenue dans l'application Enquêteur Pro", font=("Helvetica", 16),
                              bg="white")
        self.label.pack(pady=20)

        # * Add a button
        self.button = tk.Button(self.frame, text="Commencer", font=("Helvetica", 12), command=on_button_click)
        self.button.pack(pady=20)


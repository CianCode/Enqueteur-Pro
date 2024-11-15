# interface.py

import tkinter as tk
from tkinter import messagebox

from controllers.database_controller import DatabaseController


class DatabaseApp:
    def __init__(self, root):
        # Setup the main window
        self.root = root
        self.root.title("PostgreSQL Version Checker")
        self.root.geometry("400x200")

        # Create a label to display the PostgreSQL version
        self.version_label = tk.Button(root, text="PostgreSQL Version will appear here.", font=("Arial", 14))
        self.version_label.pack(pady=20)

        # Create a button to trigger the database version check
        self.check_version_button = tk.Button(root, text="Check Version", command=self.check_version, font=("Arial", 12))
        self.check_version_button.pack()

        # Initialize the DatabaseController
        self.db_controller = DatabaseController()

    def check_version(self):
        """Handle the button click event to get the database version."""
        try:
            # Connect to the database
            self.db_controller.connect()

            # Get the PostgreSQL version
            version = self.db_controller.get_version()

            # Display the version in the label
            self.version_label.config(text=f"PostgreSQL Version: {version[0][0]}")

            # Close the connection
            self.db_controller.close_connection()

        except Exception as e:
            # Show an error message if the connection fails
            messagebox.showerror("Database Error", f"Failed to connect to the database:\n{e}")
            self.version_label.config(text="Error retrieving version.")

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
    def __init__(self, parent, show_content1_callback, show_content2_callback, show_content3_callback):
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


class EnqueteFrame(tk.Frame):
    def __init__(self, parent, show_details_callback, controller):
        super().__init__(parent, bg="#ECF0F1")
        self.controller = controller  # Instance of InvestigateurController

        # Callback function to show investigation details
        self.show_details_callback = show_details_callback

        self.label = tk.Label(self, text="Select an Investigation", font=("Arial", 20, "bold"), bg="#ECF0F1", fg="#34495E")
        self.label.pack(pady=20)

        # List of investigations
        self.list_frame = tk.Frame(self, bg="#ECF0F1")
        self.list_frame.pack(pady=30, padx=20, fill=tk.Y, expand=True)

        self.investigation_list = tk.Listbox(self.list_frame, font=("Arial", 16), height=20, width=30)
        self.investigation_list.pack(side=tk.LEFT, fill=tk.Y, padx=5)

        # Scrollbar for the investigation list
        self.scrollbar = tk.Scrollbar(self.list_frame, command=self.investigation_list.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.investigation_list.config(yscrollcommand=self.scrollbar.set)

        # Bind the selection event
        self.investigation_list.bind("<<ListboxSelect>>", self.on_select)

        # Load initial data from the controller
        self.investigations = self.controller.list_investigations()
        self.filtered_investigations = self.investigations
        self.update_list()

    def update_list(self):
        # Assuming you have a method to fetch investigations
        investigations = self.controller.list_investigations()

        # Clear the list before adding new items
        self.investigation_list.delete(0, tk.END)

        # Insert each investigation's name into the listbox
        for inv in investigations:
            self.investigation_list.insert(tk.END, inv[1])  # Assuming inv[0] is the name of the investigation

    def on_select(self, event):
        """Handle selection of an investigation."""
        try:
            selected_index = self.investigation_list.curselection()[0]
            selected_investigation = self.filtered_investigations[selected_index]
            self.show_details_callback(selected_investigation)
        except IndexError:
            pass


class InvestigationDetailsFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#ECF0F1")
        self.label = tk.Label(self, text="Investigation", font=("Arial", 20, "bold"), bg="#ECF0F1", fg="#34495E")
        self.label.pack(pady=20)

        self.details_text = tk.Text(self, font=("Arial", 12), fg="#ECF0F1", height=20, width=60, wrap="word")
        self.details_text.pack(pady=10, padx=10)
        self.details_text.insert("1.0", "Details will be displayed here.")
        self.details_text.config(state=tk.DISABLED)  # Make the text widget read-only initially

    def update_details(self, investigation):
        """
        Update the investigation details in the Text widget.
        :param investigation: A tuple (id_investigation, name, status, date_open, date_close)
        """
        # Assuming 'investigation' is a tuple, e.g. (id_investigation, name, status, date_open, date_close)
        details = f"ID: {investigation[0]}\n"  # Accessing the ID using index 0
        details += f"Name: {investigation[1]}\n"  # Name is at index 1
        details += f"Status: {investigation[3]}\n"  # Status is at index 3
        details += f"Date Open: {investigation[4]}\n"  # Date Open is at index 4
        details += f"Date Close: {investigation[5]}\n"  # Date Close is at index 5

        # Update the details in the Text widget
        self.details_text.config(state=tk.NORMAL)  # Allow changes to the text widget
        self.details_text.delete("1.0", "end")  # Clear current text
        self.details_text.insert("1.0", details)  # Insert new details
        self.details_text.config(state=tk.DISABLED)  # Make it read-only again

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

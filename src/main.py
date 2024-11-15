import tkinter as tk
from interface.gui import DatabaseApp  # Import the DatabaseApp class
from src.controllers.investigation_controller import InvestigationController  # Import the InvestigationController class

# Create the Tkinter window and pass it to the DatabaseApp class
if __name__ == "__main__":
    controller = InvestigationController()
    root = tk.Tk()  # Initialize the root Tkinter window
    app = DatabaseApp(root, controller)  # Initialize the DatabaseApp with the root window
    root.mainloop()  # Start the Tkinter main event loop

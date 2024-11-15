# main.py

import tkinter as tk
from interface.interface import DatabaseApp

# Create the Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()

# Description: Main file to run the application

# Importing the necessary libraries
from tkinter import Tk
from interface.gui import EnqueteurProApp

def main():
    # Set up your database credentials
    db_name = 'gestion_enquete'         # Replace with your database name
    user = 'enquete_user'           # Replace with your database user
    password = 'enquete123'   # Replace with your database password
    host = '127.0.0.1'           # Replace with your host if different
    port = '5432'                # Replace with your port if different

    # GUI initialization
    root = Tk()
    app = EnqueteurProApp(root)
    root.mainloop()

    # When the GUI is closed, stop the database thread
    db_thread.stop()

if __name__ == "__main__":
    print("Starting the application...")
    main()

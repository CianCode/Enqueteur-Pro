# Description: Main file to run the application

from tkinter import Tk
from interface.gui import EnqueteurProApp

import psycopg2

if __name__ == "__main__":
    # * Postgresql connection
    try:
        conn = psycopg2.connect(
            dbname="gestion_enquete", user="enquete_user", password="enquete123", host="127.0.0.1", port="5432"
        )
        print("Connexion à la base de données réussie")
        cursor = conn.cursor()
    except Exception as e:
        print(f"Impossible de se connecter à la base de données : {e}")
        exit()

    # * GUI initialization
    root = Tk()
    app = EnqueteurProApp(root)
    root.mainloop()

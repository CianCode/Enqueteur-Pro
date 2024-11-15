import tkinter as tk
from interface.frames import ContentFrame1, ContentFrame2  # Correct module import

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Application")
        self.root.geometry("800x600")

        # Create a container for the navigation bar and content
        self.navbar = tk.Frame(self.root, bg="gray", width=100)
        self.navbar.pack(side=tk.LEFT, fill=tk.Y)

        self.content = tk.Frame(self.root)
        self.content.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Create buttons for navigation
        self.nav_button1 = tk.Button(self.navbar, text="Content 1", command=self.show_content1)
        self.nav_button1.pack(pady=10, padx=5, fill=tk.X)

        self.nav_button2 = tk.Button(self.navbar, text="Content 2", command=self.show_content2)
        self.nav_button2.pack(pady=10, padx=5, fill=tk.X)

        # Initialize frames
        self.frame1 = ContentFrame1(self.content)
        self.frame2 = ContentFrame2(self.content)

        # Place both frames in the same location
        self.frame1.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Show the first frame by default
        self.show_content1()

    def show_content1(self):
        self.frame2.lower()  # Send frame2 to the back
        self.frame1.lift()  # Bring frame1 to the front

    def show_content2(self):
        self.frame1.lower()  # Send frame1 to the back
        self.frame2.lift()  # Bring frame2 to the front

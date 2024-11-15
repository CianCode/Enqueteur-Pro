import tkinter as tk

class ContentFrame1(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="This is Content 1", font=("Arial", 16))
        label.pack(pady=20)

class ContentFrame2(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        label = tk.Label(self, text="This is Content 2", font=("Arial", 16))
        label.pack(pady=20)

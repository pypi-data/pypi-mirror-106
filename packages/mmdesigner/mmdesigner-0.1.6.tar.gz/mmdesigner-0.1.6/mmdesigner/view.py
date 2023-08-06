import tkinter as tk

def get_root_window():
        root = tk.Tk(className="mmdesigner")
        root.withdraw()
        root.title("mmdesigner")
        return root

import tkinter as tk
from PIL import ImageTk as itk

from .menubar import MenuBar


class Gui(tk.Tk):

    def __init__(self, name, size):
        super().__init__(className=name)
        self.title(name)
        self.withdraw()
        self.geometry(size)
        self.protocol('WM_DELETE_WINDOW', self.quit)
        menubar = MenuBar(self)
        self.config(menu=menubar)

    def get_main_window(self):
        self.set_icon()
        return self

    def set_icon(self):
        iconphoto = "mmdesigner/lpp.png"
        photo = itk.PhotoImage(file = iconphoto)
        self.iconphoto(False, photo)


    def quit(self):
        self.destroy()

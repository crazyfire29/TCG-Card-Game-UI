import tkinter


class CardRandomFrame(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg="#AE905E", width=800, height=800)
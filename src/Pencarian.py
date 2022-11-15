from pathlib import Path
import tkinter as tk
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/Pencarian")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Pencarian(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Pencarian()


    def Pencarian(self):
        self.canvas = Canvas(
            self.master,
            bg = "#D4F1F4",
            height = 738,
            width = 1366,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1366.0,
            90.0,
            fill="#05445E",
            outline="")

        self.button_pencarian = PhotoImage(
            file=relative_to_assets("pencarian.png"))
        self.pencarian = Button(
            image=self.button_pencarian,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("pencarian clicked"),
            relief="flat"
        )
        self.pencarian.place(
            x=1244.0,
            y=0.0,
            width=90.0,
            height=90.0
        )

        # self.canvas.create_text(
        #     130.0,
        #     25.0,
        #     anchor="nw",
        #     text="Masukkan Keyword",
        #     fill="#817C7C",
        #     font=("MontserratRoman SemiBold", 35 * -1)
        # )

        self.entry_1 = Entry(
            bd=0,
            bg="#05445E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=130.0,
            y=25.0,
            width=300.0,
            height=50.0
        )

        self.button_back = PhotoImage(
            file=relative_to_assets("back.png"))
        self.back = Button(
            image=self.button_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Menu(), #print("back clicked"),
            relief="flat"
        )
        self.back.place(
            x=25.0,
            y=0.0,
            width=90.0,
            height=90.0
        )
    def startPage(self):
        self.mainloop()
    
    def _on_click_Menu(self):
        self.origin.Menu()

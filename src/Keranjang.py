from pathlib import Path
import tkinter as tk
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/Keranjang")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Keranjang(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Keranjang()


    def Keranjang(self):
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

        self.canvas.create_text(
            130.0,
            25.0,
            anchor="nw",
            text="Keranjang",
            fill="#FFFFFF",
            font=("MontserratRoman SemiBold", 35 * -1)
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

        self.canvas.create_text(
            328.0,
            146.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            328.0,
            185.0,
            anchor="nw",
            text="Rp18.900",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.image_makanan1 = PhotoImage(
            file=relative_to_assets("makanan1.png"))
        self.makanan1 = self.canvas.create_image(
            210.0,
            183.0,
            image=self.image_makanan1
        )

        self.canvas.create_rectangle(
            0.0,
            648.0,
            1366.0,
            738.0,
            fill="#05445E",
            outline="")

        self.canvas.create_text(
            95.0,
            671.0,
            anchor="nw",
            text="Harga Total",
            fill="#FFFFFF",
            font=("MontserratRoman SemiBold", 33 * -1)
        )

        self.canvas.create_text(
            1130.0,
            162.0,
            anchor="nw",
            text="Rp75.600",
            fill="#000000",
            font=("MontserratRoman Medium", 30 * -1)
        )

        self.button_delete = PhotoImage(
            file=relative_to_assets("delete.png"))
        self.delete = Button(
            image=self.button_delete,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("delete clicked"),
            relief="flat"
        )
        self.delete.place(
            x=969.0,
            y=162.0,
            width=35.0,
            height=35.0
        )

        self.button_min = PhotoImage(
            file=relative_to_assets("min.png"))
        self.min = Button(
            image=self.button_min,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("min clicked"),
            relief="flat"
        )
        self.min.place(
            x=787.0,
            y=162.0,
            width=35.0,
            height=35.0
        )

        self.button_plus = PhotoImage(
            file=relative_to_assets("plus.png"))
        self.plus = Button(
            image=self.button_plus,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("plus clicked"),
            relief="flat"
        )
        self.plus.place(
            x=909.0,
            y=162.0,
            width=35.0,
            height=35.0
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            867.0,
            180.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#05445E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=852.0,
            y=160.0,
            width=30.0,
            height=38.0
        )

        self.button_pesan = PhotoImage(
            file=relative_to_assets("pesan.png"))
        self.pesan = Button(
            image=self.button_pesan,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_KonfirmasiPesanan(), #print("pesan clicked"),
            relief="flat"
        )
        self.pesan.place(
            x=1168.0,
            y=660.0,
            width=176.0,
            height=64.0
        )
    
    def startPage(self):
        self.mainloop()

    def _on_click_Menu(self):
        self.origin.Menu()
    
    def _on_click_KonfirmasiPesanan(self):
        self.origin.KonfirmasiPesanan()
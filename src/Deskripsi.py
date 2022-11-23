from pathlib import Path
import tkinter as tk
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/Deskripsi")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class DeskripsiPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Deskripsi()


    def Deskripsi(self):
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

        self.button_nextdesc = PhotoImage(
            file=relative_to_assets("nextdesc.png"))
        self.nextdesc = Button(
            image=self.button_nextdesc,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("nextdesc clicked"),
            relief="flat"
        )
        self.nextdesc.place(
            x=1045.0,
            y=610.0,
            width=56.0,
            height=56.0
        )

        self.button_backdesc = PhotoImage(
            file=relative_to_assets("backdesc.png"))
        self.backdesc = Button(
            image=self.button_backdesc,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("backdesc clicked"),
            relief="flat"
        )
        self.backdesc.place(
            x=249.0,
            y=610.0,
            width=56.0,
            height=56.0
        )

        self.button_tambahkankekeranjang = PhotoImage(
            file=relative_to_assets("TambahkanKeKeranjang.png"))
        self.TambahkanKeKeranjang = Button(
            image=self.button_tambahkankekeranjang,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("TambahkanKeKeranjang clicked"),
            relief="flat"
        )
        self.TambahkanKeKeranjang.place(
            x=380.0,
            y=610.0,
            width=590.0,
            height=56.0
        )

        self.canvas.create_text(
            604.0,
            509.0,
            anchor="nw",
            text="Stok Tersedia",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
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
            x=610.0,
            y=550.0,
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
            x=732.0,
            y=550.0,
            width=35.0,
            height=35.0
        )

        self.canvas.create_text(
            600.0,
            400.0,
            anchor="nw",
            text="Rp18.900",
            fill="#000000",
            font=("MontserratRoman SemiBold", 45 * -1)
        )

        self.canvas.create_text(
            600.0,
            290.0,
            anchor="nw",
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ",
            fill="#000000",
            font=("MontserratRoman Regular", 25 * -1)
        )

        self.canvas.create_text(
            600.0,
            235.0,
            anchor="nw",
            text="Makanan",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            600.0,
            190.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 40 * -1)
        )

        self.image_makanan = PhotoImage(
            file=relative_to_assets("makanan.png"))
        self.makanan = self.canvas.create_image(
            311.0,
            312.0,
            image=self.image_makanan
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            690.0,
            568.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#05445E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=675.0,
            y=548.0,
            width=30.0,
            height=38.0
        )

        self.image_PesanSini = PhotoImage(
            file=relative_to_assets("PesanSini.png"))
        self.PesanSini = self.canvas.create_image(
            284.0,
            45.0,
            image=self.image_PesanSini
        )

        self.button_keranjang = PhotoImage(
            file=relative_to_assets("keranjang.png"))
        self.keranjang = Button(
            image=self.button_keranjang,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Keranjang(), #print("keranjang clicked"),
            relief="flat"
        )
        self.keranjang.place(
            x=1244.0,
            y=0.0,
            width=90.0,
            height=90.0
        )

        self.button_pencarian = PhotoImage(
            file=relative_to_assets("pencarian.png"))
        self.pencarian = Button(
            image=self.button_pencarian,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Pencarian(), #print("pencarian clicked"),
            relief="flat"
        )
        self.pencarian.place(
            x=1154.0,
            y=0.0,
            width=90.0,
            height=90.0
        )
    def startPage(self):
        self.mainloop() 

    def _on_click_Keranjang(self):
        self.origin.Keranjang()

    def _on_click_Menu(self):
        self.origin.Menu()
    
    def _on_click_Pencarian(self):
        self.origin.Pencarian()   

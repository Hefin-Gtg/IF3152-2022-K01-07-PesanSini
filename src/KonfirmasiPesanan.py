from pathlib import Path
import tkinter as tk
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/KonfirmasiPesanan")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class KonfirmasiPesananPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.KonfirmasiPesanan()


    def KonfirmasiPesanan(self):
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
            text="Konfirmasi Pesanan",
            fill="#FFFFFF",
            font=("MontserratRoman SemiBold", 35 * -1)
        )

        self.button_back = PhotoImage(
            file=relative_to_assets("back.png"))
        self.back = Button(
            image=self.button_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Keranjang(), #print("back clicked"),
            relief="flat"
        )
        self.back.place(
            x=25.0,
            y=0.0,
            width=90.0,
            height=90.0
        )

        self.canvas.create_rectangle(
            283.0,
            128.0,
            1083.0,
            328.0,
            fill="#66C6BA",
            outline="")

        self.canvas.create_text(
            475.0,
            153.0,
            anchor="nw",
            text="Masukkan nama dan no Meja",
            fill="#000000",
            font=("MontserratRoman SemiBold", 35 * -1)
        )

        self.canvas.create_rectangle(
            462.0,
            239.184326171875,
            962.99951171875,
            241.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            462.0,
            298.184326171875,
            962.99951171875,
            300.0,
            fill="#000000",
            outline="")

        self.image_nomeja = PhotoImage(
            file=relative_to_assets("nomeja.png"))
        self.nomeja = self.canvas.create_image(
            442.0,
            286.0,
            image=self.image_nomeja
        )

        self.image_nama = PhotoImage(
            file=relative_to_assets("nama.png"))
        self.nama = self.canvas.create_image(
            442.0,
            226.0,
            image=self.image_nama
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            709.0,
            219.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#66C6BA",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.nama
        )
        self.entry_1.place(
            x=463.0,
            y=203.0,
            width=492.0,
            height=31.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_2 = self.canvas.create_image(
            709.0,
            279.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#66C6BA",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.nomeja
        )
        self.entry_2.place(
            x=463.0,
            y=263.0,
            width=492.0,
            height=31.0
        )

        self.canvas.create_text(
            389.0,
            429.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            389.0,
            468.0,
            anchor="nw",
            text="Rp18.900 x 4",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.image_makanan1 = PhotoImage(
            file=relative_to_assets("makanan1.png"))
        
        self.canvas.create_image(
            250.0,
            470.0,
            image=self.image_makanan1
        )

        self.canvas.create_text(
            550.0,
            358.0,
            anchor="nw",
            text="Detail Pesanan",
            fill="#000000",
            font=("MontserratRoman SemiBold", 35 * -1)
        )

        self.canvas.create_text(
            922.0,
            448.0,
            anchor="nw",
            text="Harga",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
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

        self.button_bayar = PhotoImage(
            file=relative_to_assets("bayar.png"))
        self.bayar = Button(
            image=self.button_bayar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_DetailPesanan(self.nama, self.nomeja), #print("bayar clicked"), self.nama, self.nomeja
            relief="flat"
        )
        self.bayar.place(
            x=1168.0,
            y=660,
            width=176.0,
            height=64.0
        )
    def startPage(self):
        self.mainloop()

    def _on_click_Keranjang(self):
        self.origin.Keranjang()
        
    def _on_click_DetailPesanan(self, nama, nomeja):
        nama = self.nama
        nomeja = self.nomeja
        self.origin.DataPemesan(nama, nomeja)
        self.origin.DetailPesanan()
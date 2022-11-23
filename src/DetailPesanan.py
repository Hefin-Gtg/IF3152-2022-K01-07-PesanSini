from pathlib import Path
import tkinter as tk
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/DetailPesanan")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class DetailPesananPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.DetailPesanan()


    def DetailPesanan(self):
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
            text="Detail Pesanan",
            fill="#FFFFFF",
            font=("MontserratRoman SemiBold", 35 * -1)
        )

        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute("select ID_pesanan, nomor_meja, nama_pelanggan, harga_total from DetailPesanan ORDER BY ID_pesanan DESC LIMIT 1")
        for i, menu in enumerate(menu):
            ID_pesanan = menu[0]
            nomor_meja = menu[1]
            nama_pelanggan = menu[2]
            harga_total = menu[3]
        

        self.button_back = PhotoImage(
            file=relative_to_assets("back.png"))
        self.back = Button(
            image=self.button_back,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Menu(),
            relief="flat"
        )
        self.back.place(
            x=25.0,
            y=0.0,
            width=90.0,
            height=90.0
        )

        self.canvas.create_text(
            95.0,
            675.0,
            anchor="nw",
            text="Harga Total",
            fill="#FFFFFF",
            font=("MontserratRoman SemiBold", 33 * -1)
        )

        self.canvas.create_rectangle(
            283.0,
            193.0,
            1083.0,
            268.0,
            fill="#66C6BA",
            outline="")

        self.canvas.create_text(
            390.0,
            209.0,
            anchor="nw",
            text="Silakan Lakukan Pembayaran di Kasir!",
            fill="#000000",
            font=("MontserratRoman Bold", 35 * -1)
        )

        self.canvas.create_rectangle(
            333.0,
            312.0,
            1033.0,
            612.0,
            fill="#66C6BA",
            outline="")

        # self.canvas.create_text(
        #     350.0,
        #     520.0,
        #     anchor="nw",
        #     text=f"Harga Total       : Rp{harga_total}",
        #     fill="#000000",
        #     font=("MontserratRoman Medium", 33 * -1)
        # )

        self.canvas.create_text(
            350.0,
            340.0,
            anchor="nw",
            text=f"Nama                 : {nama_pelanggan}",
            fill="#000000",
            font=("MontserratRoman Medium", 33 * -1)
        )

        self.canvas.create_text(
            350.0,
            400.0,
            anchor="nw",
            text=f"No Meja             :{nomor_meja}",
            fill="#000000",
            font=("MontserratRoman Medium", 33 * -1)
        )

        self.canvas.create_text(
            350.0,
            460.0,
            anchor="nw",
            text=f"ID Pemesanan : {ID_pesanan}",
            fill="#000000",
            font=("MontserratRoman Medium", 33 * -1)
        )
    def startPage(self):
        self.mainloop()

    
    def _on_click_Menu(self):
        self.origin.Menu()

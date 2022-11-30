from pathlib import Path
import tkinter as tk
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/Deskripsi")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class DeskripsiPage(tk.Frame):
    def __init__(self, master, pageManager, ID_menu):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.ID_menu = ID_menu
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
            command=lambda: self._on_click_Menu(),
            relief="flat"
        )
        self.back.place(
            x=25.0,
            y=0.0,
            width=90.0,
            height=90.0
        )

        menu = self.origin.mydb.cursor(buffered = True)
        requirement = f"ID_menu= '{self.ID_menu}'"
        menu.execute("select nama_menu, harga_menu, deskripsi_menu, jenis_menu, stok_menu from menu where " + requirement)
        for i, order in enumerate(menu):
            nama_menu = order[0]
            harga_menu = order[1]
            deskripsi_menu = order[2]
            jenis_menu = order[3]
            stok_menu = order[4]

        self.button_nextdesc = PhotoImage(
            file=relative_to_assets("nextdesc.png"))
        self.nextdesc = Button(
            image=self.button_nextdesc,
            borderwidth=0,
            highlightthickness=0,
            command= lambda : self.nextmenu(),
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
            command=lambda : self.backmenu(),
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
            command=lambda ID_menu = self.ID_menu: self._on_click_TambahkanKeKeranjang(ID_menu),
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
            450.0,
            anchor="nw",
            text=self.Cekstok(stok_menu),
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            600.0,
            400.0,
            anchor="nw",
            text="Rp{:0,}".format(harga_menu),
            fill="#000000",
            font=("MontserratRoman SemiBold", 45 * -1)
        )

        self.canvas.create_text(
            600.0,
            290.0,
            anchor="nw",
            width = 750,
            text=deskripsi_menu,
            fill="#000000",
            font=("MontserratRoman Regular", 25 * -1)
        )

        self.canvas.create_text(
            600.0,
            235.0,
            anchor="nw",
            text=jenis_menu,
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            600.0,
            190.0,
            anchor="nw",
            text=nama_menu,
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
            command=lambda: self._on_click_Keranjang(),
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
            command=lambda: self._on_click_Pencarian(),
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
    
    def _on_click_TambahkanKeKeranjang(self, ID_menu):
        self.origin.TambahKeranjang(ID_menu)
    
    def Cekstok(self,stok_menu):
        if stok_menu > 0:
            return "Produk Tersedia"
        else:
            return "Produk habis"
    
    def nextmenu(self):
        if self.ID_menu != 36:
            self.ID_menu = self.ID_menu + 1
            self.origin.Deskripsi(self.ID_menu)
        else :
            self.ID_menu = 1
            self.origin.Deskripsi(self.ID_menu)
        
    def backmenu(self):
        if self.ID_menu != 1:
            self.ID_menu = self.ID_menu - 1
            self.origin.Deskripsi(self.ID_menu)
        else :
            self.ID_menu = 36
            self.origin.Deskripsi(self.ID_menu)
            

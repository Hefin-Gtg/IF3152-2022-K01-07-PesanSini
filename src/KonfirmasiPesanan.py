from pathlib import Path
import tkinter as tk
from tkinter import messagebox
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
            command=lambda: self._on_click_Keranjang(),
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
            239.0,
            963.0,
            241.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            462.0,
            298.0,
            963.0,
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

        self.Nama = tk.StringVar()
        self.Nomeja = tk.StringVar()

        self.entry_1 = Entry(
            bd=0,
            bg="#66C6BA",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.Nama
        )
        self.entry_1.place(
            x=463.0,
            y=203.0,
            width=492.0,
            height=31.0
        )

        self.entry_2 = Entry(
            bd=0,
            bg="#66C6BA",
            fg="#000716",
            highlightthickness=0,
            textvariable=self.Nomeja
        )
        self.entry_2.place(
            x=463.0,
            y=263.0,
            width=492.0,
            height=31.0
        )

        self.canvas.create_text(
            550.0,
            358.0,
            anchor="nw",
            text="Detail Pesanan",
            fill="#000000",
            font=("MontserratRoman SemiBold", 35 * -1)
        )

        self.createScrollableCanvas()

        self.button_bayar = PhotoImage(
            file=relative_to_assets("bayar.png"))
        self.bayar = Button(
            image=self.button_bayar,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_DetailPesanan(),
            relief="flat"
        )
        self.bayar.place(
            x=1168.0,
            y=660,
            width=176.0,
            height=64.0
        )
    

    def createScrollableCanvas(self):
        self.scrollcanvas = Canvas(
            self.master,
            bg = "#D4F1F4",
            height = 300,
            width = 1223,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.scrollcanvas.place(x = 65.0, y = 400.0)

        self.scroll_y = Scrollbar(self.canvas, orient="vertical", command=self.scrollcanvas.yview)
        self.scroll_y.place(x = 1288.0, y = 400.0, height = 300)

        self.frame = Frame(self.scrollcanvas, bg = "#D4F1F4")

        self.makanan = PhotoImage(
            file=relative_to_assets("makanan1.png"))
        
        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute("select nama_menu, k.ID_menu, harga_menu, kuantitas_pesanan from keranjang as k inner join menu as m where k.ID_menu = m.ID_menu" )
        
        for i, order in enumerate(menu):
            self.newCanvas = Canvas(
                self.frame, 
                width = 1043, 
                height=124,
                bd = 0,
                bg = "#05445E",
                highlightthickness = 0,
                relief = "ridge"                
            )
            nama_menu = order[0]
            ID_menu = order[1]
            harga_menu = order[2]
            kuantitas_pesanan = order[3]
            harga_total = order[2] * order[3]
            
            
            self.image = self.newCanvas.create_image(
                156.0,
                60.0,
                image=self.makanan
            )

            self.newCanvas.create_text(
                354,
                26,
                anchor="nw",
                text=nama_menu,
                fill="#FFFFFF",
                font=("MontserratRoman SemiBold", 25 * -1)
            )

            self.newCanvas.create_text(
                354,
                86,
                anchor="nw",
                text=kuantitas_pesanan,
                fill="#FFFFFF",
                font=("MontserratRoman SemiBold", 25 * -1)
            )

            self.newCanvas.create_text(
                354.0,
                56,
                anchor="nw",
                text='Rp{:0,}'.format(harga_menu),
                fill="#FFFFFF",
                font=("MontserratRoman SemiBold", 20 * -1)
            )

            self.newCanvas.grid(
                row = i,
                column=0,
                padx=10,
                pady=10
                )
        
        self.scrollcanvas.create_window(
            87,
            10, 
            anchor='nw', 
            window=self.frame
        )
        
        self.scrollcanvas.update_idletasks()
        self.scrollcanvas.configure(
            scrollregion=self.scrollcanvas.bbox('all'), 
            yscrollcommand=self.scroll_y.set
        )
    def startPage(self):
        self.mainloop()

    def _on_click_Keranjang(self):
        self.origin.Keranjang()
        
    def _on_click_DetailPesanan(self):
        try:
            nama = str(self.Nama.get())
            nomeja = str(self.Nomeja.get())
            self.origin.DataPemesan(nama, nomeja)
        except:
            messagebox.showinfo("Data yang dimasukkan tidak benar", "Silakan masukkan nama dan nomor meja yang benar")
            return False
            
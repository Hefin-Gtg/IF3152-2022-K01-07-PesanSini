from pathlib import Path
import tkinter as tk
from tkinter import *
import EditKeranjang

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/Keranjang")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class KeranjangPage(tk.Frame):
    
    harga_total_pesanan = 0
    
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.EditKeranjang = EditKeranjang
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
        self.createScrollableCanvas()
        # Title
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1366.0,
            90.0,
            fill="#05445E",
            outline=""
        )

        self.canvas.create_text(
            130.0,
            25.0,
            anchor="nw",
            text="Keranjang",
            fill="#FFFFFF",
            font=("MontserratRoman SemiBold", 35 * -1)
        )
        # Back
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
        
        #Bottom 
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
            text="Harga Total: Rp{:0,}".format(self.harga_total_pesanan),
            fill="#FFFFFF",
            font=("MontserratRoman SemiBold", 33 * -1)
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
    
    def createScrollableCanvas(self):
        self.scrollcanvas = Canvas(
            self.master,
            bg = "#D4F1F4",
            height = 500,
            width = 1200,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.scrollcanvas.place(x = 83.0, y = 121.0)

        self.scroll_y = Scrollbar(self.canvas, orient="vertical", command=self.scrollcanvas.yview)
        self.scroll_y.place(x = 1288.0, y = 121.0, height = 500)

        self.frame = Frame(self.scrollcanvas, bg = "#D4F1F4")

        self.makanan = PhotoImage(
            file=relative_to_assets("makanan1.png"))
        self.button_min = PhotoImage(
            file=relative_to_assets("min.png"))
        self.button_plus = PhotoImage(
            file=relative_to_assets("plus.png"))
        self.button_delete = PhotoImage(
            file=relative_to_assets("delete.png"))

        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute("select nama_menu, k.ID_menu, m.harga_menu, kuantitas_pesanan from keranjang as k inner join menu as m on k.ID_menu = m.ID_menu")
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
            ID_menu= order[1]
            harga_menu = order[2]
            kuantitas_pesanan = order[3]
            harga_total = order[2] * order[3]

            self.order_details = {
                "ID_menu" : order[1],
                "harga_total" : harga_total
            }
            
            self.newCanvas.create_text(
                250,
                26,
                anchor="nw",
                text=nama_menu,
                fill="#FFFFFF",
                font=("MontserratRoman SemiBold", 25 * -1)
            )
            self.newCanvas.create_image(50, 17, image = self.makanan, anchor="nw")
            
            self.newCanvas.grid(
                row = i,
                column=0,
                padx=10,
                pady=10
            )
            
            self.newCanvas.create_text(
                250.0,
                69.0,
                anchor="nw",
                text='Rp{:0,}'.format(harga_menu),
                fill="#FFFFFF",
                font=("MontserratRoman SemiBold", 20 * -1)
            )

            self.newCanvas.create_text(
                900.0,
                47.0,
                anchor="nw",
                text='Rp{:0,}'.format(harga_total),
                fill="#FFFFFF",
                font=("MontserratRoman SemiBold", 20 * -1)
            )
            self.min = Button(
                self.frame,
                image =self.button_min,
                borderwidth=0,
                highlightthickness=0,
                # command= lambda: , ini harusnya ngurangin kuantitas
                relief="flat"
            )
            self.newCanvas.create_window(
                600.0,
                45.0,
                window = self.min,
                anchor = "nw"
            )
            self.plus = Button(
                self.frame,
                image =self.button_plus,
                borderwidth=0,
                highlightthickness=0,
                # command= lambda: , ini harusnya nambah kuantitas
                relief="flat"
            )
            self.newCanvas.create_window(
                700.0,
                45.0,
                window = self.plus,
                anchor = "nw"
            )

            self.deletebutton = Button(
                self.frame,
                image = self.button_delete,
                borderwidth=0,
                highlightthickness=0,
                text = ID_menu,
                command=lambda ID_Menu = ID_menu: self.handle_delete(ID_Menu),
                relief="flat"
            )

            self.newCanvas.create_window(
                750.0,
                45.0,
                window = self.deletebutton,
                anchor = "nw"
            )

            self.harga_total_pesanan += harga_total
        
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
        
    def handle_delete(self, ID_menu):
        self.origin.HapusKeranjang(ID_menu)
        # self.EditKeranjang.HapusKeranjang(self, ID_menu)
        self.origin.Keranjang()
    def startPage(self):
        self.mainloop()

    def _on_click_Menu(self):
        self.origin.Menu()
    
    def _on_click_KonfirmasiPesanan(self):
        # self.origin.Pesan()
        self.origin.KonfirmasiPesanan()
        # command = 
        

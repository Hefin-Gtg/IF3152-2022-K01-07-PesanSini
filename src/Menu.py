from pathlib import Path
import tkinter as tk
from tkinter import *
# import EditKeranjang

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/Menu")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class MenuPage(tk.Frame):
    def __init__(self, master, pageManager):
        super().__init__(master)
        self.master = master
        self.origin = pageManager
        self.pack()
        self.Menu()


    def Menu(self):
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

        # PesanSini
        self.canvas.create_rectangle(
            0.0,
            0.0,
            1366.0,
            90.0,
            fill="#05445E",
            outline="")
        self.image_PesanSini = PhotoImage(
            file=relative_to_assets("PesanSini.png"))
        self.PesanSini = self.canvas.create_image(
            284.0,
            45.0,
            image=self.image_PesanSini
        )

        # Keranjang
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
        
        # Pencarian
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
        
        # KATEGORI
        self.canvas.create_rectangle(
            0.0,
            107.0,
            1366.0,
            157.0,
            fill="#05445E",
            outline="")
        self. kategori = 'makanan'
        self.createScrollableCanvas()

        # makanan
        self.button_makanan = PhotoImage(
            file=relative_to_assets("makanan.png"))
        self.makanan = Button(
            image=self.button_makanan,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self._on_click_makanan(),
            relief="flat"
        )
        self.makanan.place(
            x=115.0,
            y=107.0,
            width=188.0,
            height=50.0
        )
        # minuman
        self.button_minuman = PhotoImage(
            file=relative_to_assets("minuman.png"))
        self.minuman = Button(
            image=self.button_minuman,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self._on_click_minuman(),
            relief="flat"
        )
        self.minuman.place(
            x=303.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        # coffee
        self.button_coffee = PhotoImage(
            file=relative_to_assets("coffee.png"))
        self.coffee = Button(
            image=self.button_coffee,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self._on_click_coffee(),
            relief="flat"
        )
        self.coffee.place(
            x=491.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        # topping
        self.button_topping = PhotoImage(
            file=relative_to_assets("topping.png"))
        self.topping = Button(
            image=self.button_topping,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self._on_click_topping(),
            relief="flat"
        )
        self.topping.place(
            x=679.0,
            y=107.0,
            width=188.0,
            height=50.0
        )
        
        # snack
        self.button_snack = PhotoImage(
            file=relative_to_assets("snack.png"))
        self.snack = Button(
            image=self.button_snack,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self._on_click_snack(),
            relief="flat"
        )
        self.snack.place(
            x=867.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        # paket
        self.button_paket = PhotoImage(
            file=relative_to_assets("paket.png"))
        self.paket = Button(
            image=self.button_paket,
            borderwidth=0,
            highlightthickness=0,
            command= lambda: self._on_click_paket(),
            relief="flat"
        )
        self.paket.place(
            x=1055.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

    def createScrollableCanvas(self):
        self.scrollcanvas = Canvas(
            self.master,
            bg = "#D4F1F4",
            height = 500,
            width = 1223,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.scrollcanvas.place(x = 65.0, y = 194.0)

        self.scroll_y = Scrollbar(self.canvas, orient="vertical", command=self.scrollcanvas.yview)
        self.scroll_y.place(x = 1288.0, y = 194.0, height = 500)

        self.frame = Frame(self.scrollcanvas, bg = "#D4F1F4")

        self.button_deskripsimakanan = PhotoImage(
            file=relative_to_assets("gambarmakanan.png"))
        
        self.button_tambahkankekeranjang = PhotoImage(
            file=relative_to_assets("Button.png"))
        
        menu = self.origin.mydb.cursor(buffered = True)
        requirement = f"jenis_menu = '{self.kategori}'"
        menu.execute("select nama_menu, ID_menu, harga_menu from menu where " + requirement)
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
            
            self.newCanvas.create_text(
                354,
                26,
                anchor="nw",
                text=nama_menu,
                fill="#FFFFFF",
                font=("MontserratRoman SemiBold", 25 * -1)
            )
            
            self.deskripsimakanan = Button(
                self.frame,
                image =self.button_deskripsimakanan,
                borderwidth=0,
                highlightthickness=0,
                command= lambda: self._on_click_Deskripsi(),
                relief="flat"
            )
            self.newCanvas.create_window(
                156.0,
                19.0,
                window = self.deskripsimakanan,
                anchor = "nw"
            )

            self.newCanvas.create_text(
                354.0,
                69.0,
                anchor="nw",
                text='Rp{:0,}'.format(harga_menu),
                fill="#FFFFFF",
                font=("MontserratRoman SemiBold", 20 * -1)
            )

            self.keranjang = Button(
                self.frame,
                image =self.button_tambahkankekeranjang,
                borderwidth=0,
                highlightthickness=0,
                command= lambda ID_Menu = ID_menu : self._on_click_TambahkanKeKeranjang(ID_Menu),
                relief="flat"
            )
            self.newCanvas.create_window(
                720.0,
                49.0,
                window = self.keranjang,
                anchor = "nw"
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

    def _on_click_Deskripsi(self):
        self.origin.Deskripsi()
    
    def _on_click_Pencarian(self):
        self.origin.Pencarian()
    
    def _on_click_makanan(self):
        self.kategori = 'makanan'
        self.createScrollableCanvas()
    
    def _on_click_minuman(self):
        self.kategori = 'minuman'
        self.createScrollableCanvas()
    
    def _on_click_coffee(self):
        self.kategori = 'coffee'
        self.createScrollableCanvas()

    def _on_click_topping(self):
        self.kategori = 'topping'
        self.createScrollableCanvas()
    
    def _on_click_snack(self):
        self.kategori = 'snack'
        self.createScrollableCanvas()
    
    def _on_click_paket(self):
        self.kategori = 'paket'
        self.createScrollableCanvas()

    def _on_click_TambahkanKeKeranjang(self, text):
        self.origin.TambahKeranjang(text)
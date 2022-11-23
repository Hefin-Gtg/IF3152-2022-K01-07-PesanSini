from pathlib import Path
import tkinter as tk
from tkinter import *
# from .Menu import MenuPage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/Pencarian")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class PencarianPage(tk.Frame):
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
            command=lambda: self.searchmenu(),
            relief="flat"
        )
        self.pencarian.place(
            x=1244.0,
            y=0.0,
            width=90.0,
            height=90.0
        )

        self.entry_1 = Entry(
            bd=0,
            bg="#05394F", #05445E",
            fg="#FFFFFF",
            highlightthickness=0,
            insertbackground = "#FFFFFF",
            font=("Calibri", 40 * -1)
        )
        self.entry_1.place(
            x=130.0,
            y=15.0,
            width=1100.0,
            height=60.0
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

    def _on_click_Deskripsi(self):
        self.origin.Deskripsi()

    def _on_click_TambahkanKeKeranjang(self, text):
        self.origin.TambahKeranjang(text)
        
    def searchmenu(self):
        self.createScrollableCanvas()
        menu = self.origin.mydb.cursor(buffered = True)
        keyword = self.entry_1.get()
        print(keyword)
        menu.execute(f"select nama_menu, ID_menu, harga_menu from menu where nama_menu like '%{keyword}%'")
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
            
            self.newCanvas.grid(
                row = i,
                column=0,
                padx=10,
                pady=10
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
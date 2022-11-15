from pathlib import Path
import tkinter as tk
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("../img/Menu")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Menu(tk.Frame):
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
        self.button_keranjang1 = PhotoImage(
            file=relative_to_assets("TambahkanKeKeranjang.png"))
        self.Keranjang1 = Button(
            image=self.button_keranjang1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Keranjang1 clicked"),
            relief="flat"
        )
        self.Keranjang1.place(
            x=285.0,
            y=281.0,
            width=210.0,
            height=30.0
        )

        self.canvas.create_text(
            285.0,
            208.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            285.0,
            247.0,
            anchor="nw",
            text="Rp18.900",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.button_makanan1 = PhotoImage(
            file=relative_to_assets("gambarmakanan.png"))
        self.makanan1 = Button(
            image=self.button_makanan1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Deskripsi(), #print("makanan1 clicked"),
            relief="flat"
        )
        self.makanan1.place(
            x=87.0,
            y=217.0,
            width=160.0,
            height=90.0
        )

        self.canvas.create_rectangle(
            0.0,
            107.0,
            1366.0,
            157.0,
            fill="#05445E",
            outline="")

        self.button_makanan = PhotoImage(
            file=relative_to_assets("makanan.png"))
        self.makanan = Button(
            image=self.button_makanan,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("makanan clicked"),
            relief="flat"
        )
        self.makanan.place(
            x=115.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            1366.0,
            90.0,
            fill="#05445E",
            outline="")

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

        self.button_minuman = PhotoImage(
            file=relative_to_assets("minuman.png"))
        self.minuman = Button(
            image=self.button_minuman,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("minuman clicked"),
            relief="flat"
        )
        self.minuman.place(
            x=303.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        self.button_coffee = PhotoImage(
            file=relative_to_assets("coffee.png"))
        self.coffee = Button(
            image=self.button_coffee,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("coffee clicked"),
            relief="flat"
        )
        self.coffee.place(
            x=491.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        self.button_topping = PhotoImage(
            file=relative_to_assets("topping.png"))
        self.topping = Button(
            image=self.button_topping,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("topping clicked"),
            relief="flat"
        )
        self.topping.place(
            x=679.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        self.button_snack = PhotoImage(
            file=relative_to_assets("snack.png"))
        self.snack = Button(
            image=self.button_snack,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("snack clicked"),
            relief="flat"
        )
        self.snack.place(
            x=867.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        self.button_paket = PhotoImage(
            file=relative_to_assets("paket.png"))
        self.paket = Button(
            image=self.button_paket,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("paket clicked"),
            relief="flat"
        )
        self.paket.place(
            x=1055.0,
            y=107.0,
            width=188.0,
            height=50.0
        )

        self.button_keranjang2 = PhotoImage(
            file=relative_to_assets("TambahkanKeKeranjang.png"))
        self.Keranjang2 = Button(
            image=self.button_keranjang2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Keranjang2 clicked"),
            relief="flat"
        )
        self.Keranjang2.place(
            x=1010.0,
            y=281.0,
            width=210.0,
            height=30.0
        )

        self.canvas.create_text(
            1010.0,
            208.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            1010.0,
            247.0,
            anchor="nw",
            text="Rp18.900",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.button_makanan2 = PhotoImage(
            file=relative_to_assets("gambarmakanan.png"))
        self.makanan2 = Button(
            image=self.button_makanan2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Deskripsi(), #print("makanan2 clicked"),
            relief="flat"
        )
        self.makanan2.place(
            x=812.0,
            y=217.0,
            width=160.0,
            height=90.0
        )

        self.button_keranjang3 = PhotoImage(
            file=relative_to_assets("TambahkanKeKeranjang.png"))
        self.Keranjang3 = Button(
            image=self.button_keranjang3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Keranjang3 clicked"),
            relief="flat"
        )
        self.Keranjang3.place(
            x=285.0,
            y=444.0,
            width=210.0,
            height=30.0
        )

        self.canvas.create_text(
            285.0,
            371.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            285.0,
            410.0,
            anchor="nw",
            text="Rp18.900",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.button_makanan3 = PhotoImage(
            file=relative_to_assets("gambarmakanan.png"))
        self.makanan3 = Button(
            image=self.button_makanan3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Deskripsi(), # print("makanan3 clicked"),
            relief="flat"
        )
        self.makanan3.place(
            x=87.0,
            y=380.0,
            width=160.0,
            height=90.0
        )

        self.button_keranjang4 = PhotoImage(
            file=relative_to_assets("TambahkanKeKeranjang.png"))
        self.Keranjang4 = Button(
            image=self.button_keranjang4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Keranjang4 clicked"),
            relief="flat"
        )
        self.Keranjang4.place(
            x=1010.0,
            y=444.0,
            width=210.0,
            height=30.0
        )

        self.canvas.create_text(
            1010.0,
            371.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            1010.0,
            410.0,
            anchor="nw",
            text="Rp18.900",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.button_makanan4 = PhotoImage(
            file=relative_to_assets("gambarmakanan.png"))
        self.makanan4 = Button(
            image=self.button_makanan4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Deskripsi(), # print("makanan4 clicked"),
            relief="flat"
        )
        self.makanan4.place(
            x=812.0,
            y=380.0,
            width=160.0,
            height=90.0
        )

        self.button_Keranjang5 = PhotoImage(
            file=relative_to_assets("TambahkanKeKeranjang.png"))
        self.Keranjang5 = Button(
            image=self.button_Keranjang5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Keranjang5 clicked"),
            relief="flat"
        )
        self.Keranjang5.place(
            x=285.0,
            y=615.0,
            width=210.0,
            height=30.0
        )

        self.canvas.create_text(
            285.0,
            542.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            285.0,
            581.0,
            anchor="nw",
            text="Rp18.900",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.button_makanan5 = PhotoImage(
            file=relative_to_assets("gambarmakanan.png"))
        self.makanan5 = Button(
            image=self.button_makanan5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Deskripsi(), #print("makanan5 clicked"),
            relief="flat"
        )
        self.makanan5.place(
            x=87.0,
            y=551.0,
            width=160.0,
            height=90.0
        )

        self.button_keranjang6 = PhotoImage(
            file=relative_to_assets("TambahkanKeKeranjang.png"))
        self.Keranjang6 = Button(
            image=self.button_keranjang6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("Keranjang6 clicked"),
            relief="flat"
        )
        self.Keranjang6.place(
            x=1010.0,
            y=615.0,
            width=210.0,
            height=30.0
        )

        self.canvas.create_text(
            1010.0,
            542.0,
            anchor="nw",
            text="Nasi Goreng",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.canvas.create_text(
            1010.0,
            581.0,
            anchor="nw",
            text="Rp18.900",
            fill="#000000",
            font=("MontserratRoman SemiBold", 25 * -1)
        )

        self.button_makanan6 = PhotoImage(
            file=relative_to_assets("gambarmakanan.png"))
        self.makanan6 = Button(
            image=self.button_makanan6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self._on_click_Deskripsi(), #print("makanan6 clicked"),
            relief="flat"
        )
        self.makanan6.place(
            x=812.0,
            y=551.0,
            width=160.0,
            height=90.0
        )

        self.image_PesanSini = PhotoImage(
            file=relative_to_assets("PesanSini.png"))
        self.PesanSini = self.canvas.create_image(
            284.0,
            45.0,
            image=self.image_PesanSini
        )
    
    def startPage(self):
        self.mainloop()

    def _on_click_Keranjang(self):
        self.origin.Keranjang()

    def _on_click_Deskripsi(self):
        self.origin.Deskripsi()
    
    def _on_click_Pencarian(self):
        self.origin.Pencarian()
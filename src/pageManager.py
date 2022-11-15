import Keranjang, Menu, KonfirmasiPesanan, Pencarian, DetailPesanan, Deskripsi
import mysql.connector
from tkinter import Tk

class pageManager():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host= "localhost", 
            user="root", 
            password="Password", 
            database = "PesanSini"
        )

        self.user = None
        self.window = Tk()
        self.window.geometry("1366x738")
        self.window.configure(bg = "#C8F4DE")
        self.window.title('PesanSini')
        self.window.resizable(False, False)
        
        self.page = Menu.Menu(master = self.window, pageManager = self)

    def run(self):
        self.page.startPage()
    
    def Menu(self):
        self.page = Menu.Menu(master = self.window, pageManager = self)
        self.page.startPage()

    def DetailPesanan(self):
        self.page = DetailPesanan.DetailPesanan(master = self.window, pageManager = self)
        self.page.startPage()
    
    def Keranjang(self):
        self.page = Keranjang.Keranjang(master = self.window, pageManager = self)
        self.page.startPage()
    
    def Deskripsi(self):
        self.page = Deskripsi.Deskripsi(master = self.window, pageManager = self)
        self.page.startPage()

    def Pencarian(self):
        self.page = Pencarian.Pencarian(master = self.window, pageManager = self)
        self.page.startPage()

    def KonfirmasiPesanan(self):
        self.page = KonfirmasiPesanan.KonfirmasiPesanan(master = self.window, pageManager = self)
        self.page.startPage()


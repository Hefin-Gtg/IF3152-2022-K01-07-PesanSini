import Keranjang, Menu, KonfirmasiPesanan, Pencarian, DetailPesanan, Deskripsi, EditKeranjang
import mysql.connector
from tkinter import Tk


class pageManager():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host= "localhost", 
            user="root", 
            password="peachytrashy2", 
            database = "PesanSini"
        )
        # self.EditKeranjang = EditKeranjang
        self.user = None
        self.window = Tk()
        self.window.geometry("1366x738")
        self.window.configure(bg = "#C8F4DE")
        self.window.title('PesanSini')
        self.window.resizable(False, False)
        
        self.page = Menu.MenuPage(master = self.window, pageManager = self)

    def run(self):
        self.page.startPage()
    
    def Menu(self):
        self.page = Menu.MenuPage(master = self.window, pageManager = self)
        self.page.startPage()

    def DetailPesanan(self):
        self.page = DetailPesanan.DetailPesananPage(master = self.window, pageManager = self)
        self.page.startPage()
    
    def Keranjang(self):
        self.page = Keranjang.KeranjangPage(master = self.window, pageManager = self)
        self.page.startPage()
    
    def Deskripsi(self):
        self.page = Deskripsi.DeskripsiPage(master = self.window, pageManager = self)
        self.page.startPage()

    def Pencarian(self):
        self.page = Pencarian.PencarianPage(master = self.window, pageManager = self)
        self.page.startPage()

    def KonfirmasiPesanan(self):
        self.page = KonfirmasiPesanan.KonfirmasiPesananPage(master = self.window, pageManager = self)
        self.page.startPage()

    def TambahKeranjang(self, text):
        self.page = EditKeranjang.EditKeranjangPage(master=self.window, pageManager=self)
        self.page.TambahKeranjang(text)

    def HapusKeranjang(self, text):
        self.page = EditKeranjang.EditKeranjangPage(master=self.window, pageManager=self)
        self.page.HapusKeranjang(text)
        
    def Pesan(self):
        self.page = EditKeranjang.EditKeranjangPage(master=self.window, pageManager=self)
        self.page.Pesan()

    def DataPemesan(self, entry1, entry2):
        self.page = EditKeranjang.EditKeranjangPage(master=self.window, pageManager=self)
        self.page.DataPemesan(entry1, entry2)
from datetime import datetime
from tkinter import messagebox

class EditKeranjangPage():
    def __init__(self, master, pageManager):
        self.master = master
        self.origin = pageManager

    def HapusKeranjang(self, ID_menu):
        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute(f"select kuantitas_pesanan from keranjang where ID_menu = {ID_menu}")
        kuantitas_pesanan = menu.fetchone()[0]
        menu.execute(f"update menu set stok_menu = stok_menu + {kuantitas_pesanan} where ID_menu = {ID_menu}")
        self.origin.mydb.commit()
        keranjang = self.origin.mydb.cursor(buffered = True)
        keranjang.execute(f"delete from keranjang where ID_menu={ID_menu}")
        self.origin.mydb.commit()

    def TambahKeranjangBaru(self, ID_menu):
        ID_menu = int(ID_menu)
        kuantitas_pesanan = 1
        Values = f"({ID_menu}, {kuantitas_pesanan})"
        keranjang = self.origin.mydb.cursor(buffered = True)
        keranjang.execute("insert into keranjang(ID_menu, kuantitas_pesanan) VALUES " + Values )
        self.origin.mydb.commit()
    
    def TambahKeranjang (self, ID_menu):
        keranjang = self.origin.mydb.cursor(buffered = True)
        keranjang.execute(f"select stok_menu from menu where ID_menu = {ID_menu}")
        if keranjang.fetchone()[0] > 0:
            keranjang.execute(f"select ID_keranjang from keranjang where ID_menu = {ID_menu}")
            if keranjang.rowcount == 0:
                self.TambahKeranjangBaru(ID_menu)
            else:
                ID_keranjang = keranjang.fetchone()[0]
                self.TambahMenu(ID_keranjang, ID_menu)
            self.KurangStok(ID_menu)
        else :
            messagebox.showinfo("Stok habis", "Stok habis, silakan pesan produk lainnya.")
    
    def Pesan(self, ID_pesanan):
        pesan =  self.origin.mydb.cursor(buffered = True)
        pesan.execute(f"insert into pesanan(ID_keranjang, ID_menu, kuantitas_pesanan)  select * from keranjang")
        pesan.execute(f"update pesanan set ID_pesanan = {ID_pesanan} where ID_pesanan is NULL")
        pesan.execute("delete from keranjang")
        self.origin.mydb.commit()

    def DataPemesan(self, nama, nomeja):
        if int(nomeja) > 20 or int(nomeja) < 0 or nama.replace(" ","") =="" :
            messagebox.showinfo("Data yang dimasukkan tidak benar", "Silakan masukkan nomor meja 0-20 atau silakan masukkan nama Anda")
        else:
            pesan =  self.origin.mydb.cursor(buffered = True)
            pesan.execute("select sum(harga_menu*kuantitas_pesanan) from keranjang as k inner join menu as m where k.ID_menu = m.ID_menu") 
            harga_total = pesan.fetchone()[0]
            timestamp = datetime.now()
            timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S')
            nama = nama.replace(" ","")
            Values = f"({nomeja}, '{nama}', {harga_total}, '{timestamp}')"
            pesan.execute(f"insert into DetailPesanan(nomor_meja, nama_pelanggan, harga_total, timestamp) values " + Values)
            self.origin.mydb.commit()
            pesan.execute(f"select ID_pesanan from DetailPesanan ORDER BY ID_pesanan DESC LIMIT 1")
            ID_pesanan = pesan.fetchone()[0]
            self.origin.Pesan(ID_pesanan)
            self.origin.DetailPesanan()
        
    def TambahMenu(self, ID_keranjang, ID_menu):
        keranjang = self.origin.mydb.cursor(buffered = True)
        keranjang.execute(f"select stok_menu from menu where ID_menu = {ID_menu}")
        if keranjang.fetchone()[0] > 0:
            keranjang.execute(f"update keranjang set kuantitas_pesanan = kuantitas_pesanan+ 1 where ID_keranjang = {ID_keranjang}")
            self.origin.mydb.commit()
        else :
            messagebox.showinfo("Stok habis", "Stok habis, silakan pesan produk lainnya.")
        
    
    def KurangMenu(self, ID_keranjang, ID_menu):
        keranjang = self.origin.mydb.cursor(buffered = True)
        keranjang.execute(f"select kuantitas_pesanan from keranjang where ID_menu = {ID_menu}")
        kuantitas_pesanan = keranjang.fetchone()[0]
        if kuantitas_pesanan > 1:
            keranjang.execute(f"update keranjang set kuantitas_pesanan = kuantitas_pesanan - 1 where ID_keranjang = {ID_keranjang}")
            self.origin.mydb.commit()
        else:
            self.HapusKeranjang(ID_menu)
        self.TambahStok(ID_menu)

    def TambahStok(self, ID_menu):
        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute(f"update menu set stok_menu = stok_menu + 1 where ID_menu = {ID_menu}")
        self.origin.mydb.commit()

    def KurangStok(self, ID_menu):
        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute(f"update menu set stok_menu = stok_menu - 1 where ID_menu = {ID_menu}")
        self.origin.mydb.commit()

    def harga_total_pesanan(self):
        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute(f"select sum(kuantitas_pesanan*harga_menu) from keranjang inner join menu")
        return menu.fetchone()[0]

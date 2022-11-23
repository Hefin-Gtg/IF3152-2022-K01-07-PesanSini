from tkinter import messagebox

class EditKeranjangPage():
    def __init__(self, master, pageManager):
        self.master = master
        self.origin = pageManager

    def HapusKeranjang(self, ID_keranjang, ID_menu, kuantitas_pesanan):
        MsgBox = messagebox.askquestion ('Hapus Menu','Hapus menu dari keranjang?',icon = 'warning')
        if MsgBox == 'yes':
            menu = self.origin.mydb.cursor(buffered = True)
            menu.execute(f"update menu set stok_menu = stok_menu + {kuantitas_pesanan} where ID_menu = {ID_menu}")
            self.origin.mydb.commit()
            ID_keranjang = int(ID_keranjang)
            keranjang = self.origin.mydb.cursor(buffered = True)
            keranjang.execute(f"delete from keranjang where ID_keranjang={ID_keranjang}")
            self.origin.mydb.commit()
                
    def Pesan(self, ID_pesanan):
        pesan =  self.origin.mydb.cursor(buffered = True)
        pesan.execute(f"insert into pesanan(ID_keranjang, ID_menu, kuantitas_pesanan)  select * from keranjang")
        pesan.execute(f"update pesanan set ID_pesanan = {ID_pesanan} where ID_pesanan is NULL")
        pesan.execute("truncate table keranjang")
        self.origin.mydb.commit()

    def DataPemesan(self, nama, nomeja):
        harga_total = 100000
        pesan =  self.origin.mydb.cursor(buffered = True)
        Values = f"({nomeja}, '{nama}', {harga_total})"
        pesan.execute(f"insert into DetailPesanan(nomor_meja, nama_pelanggan, harga_total) values " + Values)
        self.origin.mydb.commit()
        pesan.execute(f"select ID_pesanan from DetailPesanan ORDER BY ID_pesanan DESC LIMIT 1")
        ID_pesanan = pesan.fetchone()[0]
        self.origin.Pesan(ID_pesanan)
    
    def TambahMenu(self, ID_keranjang, ID_menu):
        keranjang = self.origin.mydb.cursor(buffered = True)
        keranjang.execute(f"update keranjang set kuantitas_pesanan = kuantitas_pesanan+ 1 where ID_keranjang = {ID_keranjang}")
        self.origin.mydb.commit()
        self.KurangStok(ID_menu)
    
    def KurangMenu(self, ID_keranjang, ID_menu, kuantitas_pesanan):
        keranjang = self.origin.mydb.cursor(buffered = True)
        if kuantitas_pesanan > 1:
            keranjang.execute(f"update keranjang set kuantitas_pesanan =kuantitas_pesanan - 1 where ID_keranjang = {ID_keranjang}")
            self.origin.mydb.commit()
        else:
            self.HapusKeranjang(ID_keranjang, ID_menu, kuantitas_pesanan)
        self.TambahStok(ID_menu)

    def TambahStok(self, ID_menu):
        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute(f"update menu set stok_menu = stok_menu + 1 where ID_menu = {ID_menu}")
        self.origin.mydb.commit()

    def KurangStok(self, ID_menu):
        menu = self.origin.mydb.cursor(buffered = True)
        menu.execute(f"update menu set stok_menu = stok_menu - 1 where ID_menu = {ID_menu}")
        self.origin.mydb.commit()

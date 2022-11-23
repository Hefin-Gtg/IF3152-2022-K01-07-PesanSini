class EditKeranjangPage():
    def __init__(self, master, pageManager):
        self.master = master
        self.origin = pageManager

    def HapusKeranjang(self, text):
        ID_menu = int(text)
        keranjang = self.origin.mydb.cursor(buffered = True)
        keranjang.execute(f"delete from keranjang where ID_menu={ID_menu}")
        self.origin.mydb.commit()

    
    def Pesan(self):
        ID_pesanan = 1
        pesan =  self.origin.mydb.cursor(buffered = True)
        pesan.execute(f"insert into pesanan(ID_pesanan, ID_keranjang, ID_menu, kuantitas_pesanan) values ({ID_pesanan}, (select ID_pesanan from keranjang)")
        self.origin.mydb.commit()

    def DataPemesan(self, entry1, entry2):
        ID_pesanan = 4
        harga_total = 100000
        entry2 = int(entry2)
        entry1 = str(entry1)
        pesan =  self.origin.mydb.cursor(buffered = True)
        pesan.execute(f"insert into DetailPesanan(ID_pesanan, nomor_meja, nama_pelanggan, harga_total) values ({ID_pesanan}, {entry2}, {entry1}, {harga_total})")
        self.origin.mydb.commit()
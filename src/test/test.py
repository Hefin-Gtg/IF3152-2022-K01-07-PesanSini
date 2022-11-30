import pytest
from pathlib import Path
import mysql.connector
import sys

sys.path.insert(1, "..")
import EditKeranjang as EditKeranjang

raw = {
    "ID_keranjang": "raw_ID_keranjang", 
    "ID_menu" : "raw_ID_menu",
    "kuantitas_pesanan" : "raw_kuantitas_pesanan"
}


class dummyPageManager():
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host= "localhost", 
            user="root", 
            password="Password", 
            database = "PesanSini"
        )
dummy = dummyPageManager()

def  test_TambahKeranjang ():
    sc = EditKeranjang.EditKeranjangPage(raw, dummy)
    ID_menu = 12
    sc.TambahKeranjang(ID_menu)

def test_HapusKeranjang():
    sc = EditKeranjang.EditKeranjangPage(raw, dummy)
    ID_menu = 12
    sc.HapusKeranjang(ID_menu)

@pytest.mark.xfail
def  test_TambahKeranjang_fail ():
    sc = EditKeranjang.EditKeranjangPage(raw, dummy)
    ID_menu = 60
    sc.TambahKeranjang(ID_menu)


@pytest.mark.xfail
def test_HapusKeranjang_fail():
    sc = EditKeranjang.EditKeranjangPage(raw, dummy)
    ID_menu = 16
    sc.HapusKeranjang(ID_menu)

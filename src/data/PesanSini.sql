create database if not exists PesanSini;

use PesanSini; 

create table if not exists menu (
	ID_menu INT PRIMARY KEY AUTO_INCREMENT,
	nama_menu VARCHAR(500) NOT NULL,
    foto_menu VARCHAR(100),
    deskripsi_menu VARCHAR(1000) NOT NULL,
    harga_menu INT NOT NULL,
    jenis_menu VARCHAR(100) NOT NULL,
    stok_menu INT NOT NULL
);

create table if not exists keranjang (
    ID_keranjang INT PRIMARY KEY AUTO_INCREMENT,
    ID_menu INT NOT NULL,
    kuantitas_pesanan INT NOT NULL,
    FOREIGN KEY (ID_menu)
    REFERENCES menu(ID_menu)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

create table if not exists DetailPesanan (
    ID_pesanan INT PRIMARY KEY AUTO_INCREMENT,
    nomor_meja INT NOT NULL,
    nama_pelanggan VARCHAR(500) NOT NULL,
    harga_total INT NOT NULL,
    timestamp datetime
);

create table if not exists pesanan (
    ID_pesanan INT,
    ID_keranjang INT,
    ID_menu INT,
    kuantitas_pesanan INT NOT NULL,
    PRIMARY KEY (ID_keranjang, ID_menu),
    FOREIGN KEY (ID_pesanan)
    REFERENCES DetailPesanan(ID_pesanan)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);




INSERT INTO menu(ID_menu, nama_menu, deskripsi_menu,harga_menu, jenis_menu, stok_menu) VALUES
(1, 'nasi rakyat', 'ayam suwir + tempe orek + telur dadar +sambal balado+ nasi', 18900, 'makanan', 0),
(2, 'Ayam rica-rica', 'nasi putih dengan ayam rica-rica, ditambah dengan daun kemangi, bawang, dan timun', 39900, 'makanan', 2),
(3, 'Ayam Taliwang', 'nasi putih dengan chicken karaage yang diberi bumbu taliwang, bawang goreng tabur, dan timun', 39900, 'makanan', 3),
(4, 'Cumi sambal bawang goreng', 'cumi asin+ sambal bawang goreng khas bali', 47900, 'makanan', 5),
(5, 'Cumi Pete Balado', 'cumi asin + sambal balado + kentang + pete', 47900, 'makanan', 6),
(6, 'Sapi asap lada garam', 'nasi hainan, sapi asap, bumbu lada garam, dan tumis pakcoy', 55000, 'makanan', 9),
(7, 'Almightea-Lemon Tea','Teh rasa lemon' , 18000, 'minuman', 50),
(8, 'Serenitea', 'Teh, jelly leci, dan selasih', 18000, 'minuman', 50),
(9, 'Ice Signature Chocolate', 'Ice chocolate dengan susu', 18000, 'minuman', 50),
(10, 'Ice Lemongrass Tea', 'Ice tea dengan aroma sereh', 18000, 'minuman', 50),
(11, 'Ice Green Tea', 'Ekstrak teh hijau manis dengan rasa jasmine', 18000, 'minuman', 50),
(12, 'Ice Mango Peach', 'Minuman dengan campuran rasa mangga dan peach', 22000, 'minuman', 50),
(13, 'Caramel Latte','Campuran Kopi Indonesia berkualitas dengan susu dan sirup Caramel yang bisa bikin ketagihan!', 20000, 'coffee', 50),
(14, 'Black Coffee','Kopi hitam dengan biji berkualitas yang bikin kamu melek.', 15900, 'coffee', 50),
(15, 'Hazelnut Latte','Campuran Kopi Indonesia berkualitas dengan susu dan sirup hazelnut yang cita rasanya nikmat banget!', 20000, 'coffee', 50),
(16, 'Americano','Cita rasa 100% Kopi Indonesia yang cocok banget bagi para pecinta kopi.', 15900, 'coffee', 50),
(17, 'Caffe Latte','Campuran yang pas dari Kopi Indonesia berkualitas dengan susu buat nemenin nongkrong sama siapa aja.', 19000, 'coffee', 50),
(18, 'Moccachino','Perpaduan yang pas dari Kopi,coklat ,dan susu yang bisa nemenin kamu pas lagi nugas nih.', 20000, 'coffee', 50),
(19, 'Keju Parut','Berisi keju parut', 6900, 'topping', 50),
(20, 'Sambal Matah','Berisi sambal matah',6900, 'topping', 50),
(21, 'Sambel Konslet','Berisi samabal konslet',6900, 'topping', 50),
(22, 'Sambel Domba Membara', 'Berisi sambel domba membara',6900, 'topping', 50),
(23, 'Telor Ceplok', 'Berisi telor ceplok',6900, 'topping', 50),
(24, 'Rujak ori', 'Berisi rujak ori',6900, 'topping', 50),
(25, 'Roti Prancis Coklat','Toast dengan taburan meses cokelat dan susu kental manis',18900, 'snack', 50),
(26, 'Roti Prancis Keju','Roti bakar dengan topping keju dan susu.',18900, 'snack', 50),
(27, 'Roti Prancis Coklat + Keju','Roti bakar dengan topping susu coklat dan ditaburi keju.',22900, 'snack', 50),
(28, 'Roti Prancis Milo','Toast dengan taburan bubuk milo dan susu kental manis.',22900, 'snack', 50),
(29, 'Roti Prancis Nutella','Toast dengan coklat tebal Nuttela dioleskan ke atas roti bakar crispy, enaknya luar biasa!',22900, 'snack', 50),
(30, 'Pisang Bakar Brown Sugar','Pisang nikmat yang dibakar dan ditaburi gula merah dan susu kental manis ini asik banget buat dinikmati sore-sore sambil nongkrong.',15900, 'snack', 50),
(31, 'Paket PAS Sendiri','1 nasi rakyat + 1 ice green tea',35000, 'paket', 50),
(32, 'Paket Berdua','2 nasi rakyat + 2 ice green tea',66900, 'paket', 50),
(33, 'Paket Bersama','3 Serenitea',50000, 'paket', 50),
(34, 'Paket Nugas','3 Huzelnut Latte',50900, 'paket', 50),
(35, 'Paket Nongkrong','1 Roti Prancis Coklat + 1 Roti Prancis Milo + 1 Roti Prancis Keju',63900, 'paket', 50),
(36, 'Paket Lapar','1 Ayam rica-rica + 1 Ayam Taliwang',75000, 'paket', 50);
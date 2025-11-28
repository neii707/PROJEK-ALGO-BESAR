CREATE TYPE enum_transaksi AS ENUM('dikemas', 'dikirim', 'diterima', 'selesai');
CREATE TYPE enum_pembayaran AS ENUM ('tunai', 'non tunai');

CREATE TABLE role(
id_role SERIAL PRIMARY KEY,
nama_role VARCHAR NOT NULL
);

CREATE table kategori_benih(
id_kategori_benih serial primary key,
nama_kategori Varchar(64) not null
);

CREATE TABLE keranjang_pesanan(
id_keranjang SERIAL PRIMARY KEY,
);


CREATE TABLE users(
id_user SERIAL PRIMARY KEY,
username VARCHAR(32) UNIQUE NOT NULL,
password VARCHAR(32) UNIQUE NOT NULL,
nama VARCHAR(20) NOT NULL,
no_telp VARCHAR(15) NOT NULL,

id_keranjang INTEGER REFERENCES keranjang_pesanan(id_keranjang),
id_role INTEGER REFERENCES role(id_role)
);

ALTER TABLE users
ADD CONSTRAINT fk_user_keranjang
FOREIGN KEY (id_keranjang)
REFERENCES keranjang_pesanan(id_keranjang)
ON DELETE SET NULL;


CREATE TABLE benih(
id_benih SERIAL PRIMARY KEY,
nama_benih VARCHAR(32) NOT NULL,
tanggal_masuk DATE NOT NULL,
kadaluarsa DATE NOT NULL,
harga INTEGER NOT NULL,

id_user INTEGER REFERENCES users(id_user),
id_kategori_benih INTEGER REFERENCES kategori_benih(id_kategori_benih)
);

CREATE TABLE pesanan(
id_pesanan SERIAL PRIMARY KEY,
tanggal_pesanan DATE NOT NULL,

id_user INTEGER REFERENCES users(id_user)
);

CREATE TABLE detail_keranjang(
id_detail_keranjang SERIAL PRIMARY KEY,
quantity INTEGER NOT NULL,

id_benih INTEGER REFERENCES benih(id_benih),
id_keranjang INTEGER REFERENCES keranjang_pesanan(id_keranjang)
);

CREATE TABLE detail_pesanan(
id_detail_pesanan SERIAL PRIMARY KEY,
quantity INTEGER NOT NULL,

id_pesanan INTEGER REFERENCES pesanan(id_pesanan),
id_benih INTEGER REFERENCES benih(id_benih)
);

CREATE TABLE transaksi(
id_transaksi SERIAL PRIMARY KEY,
tanggal_transaksi DATE NOT NULL,
metode_pembayaran enum_pembayaran NOT NULL,
status_transaksi enum_transaksi NOT NULL,

id_pesanan INTEGER REFERENCES pesanan(id_pesanan)
);

CREATE TABLE riwayat_produksi(
id_produksi SERIAL PRIMARY KEY,
tanggal_produksi DATE NOT NULL,
jumlah_produksi INTEGER NOT NULL,
tanggal_kadaluarsa DATE NOT NULL,

id_benih INTEGER REFERENCES benih(id_benih)
);

create table kabupaten(
id_kabupaten serial primary key,
nama varchar(32)
);

create table kecamatan(
id_kecamatan serial primary key,
nama  varchar(64),

id_kabupaten integer references kabupaten(id_kabupaten)
);

create table desa(
id_desa serial primary key,
nama varchar(64),

id_kecamatan integer references kecamatan(id_kecamatan)
);

CREATE TABLE alamat(
id_alamat SERIAL PRIMARY KEY,

id_user INTEGER REFERENCES users(id_user)
id_pesanan INTEGER REFERENCES pesanan(id_pesanan),
id_desa integer references desa(id_desa)
);

INSERT INTO role (nama_role) VALUES
('Petani'),
('Produsen'),
('Admin');

INSERT INTO users (username, password, nama, no_telp, id_keranjang, id_role) VALUES
('petani_andi', 'andi123', 'Andi Santoso', '081234567890', 1, 1),
('produsen_budi', 'budi123', 'Budi Prasetyo', '082345678901', 2, 2),
('admin_sri', 'sri123', 'Sri Lestari', '083456789012', 3, 3),
('petani_joko', 'joko123', 'Joko Susanto', '082376244616', 4, 1),
('produsen_eko', 'eko123', 'Eko Saputra', '082134567812', 5, 2),
('admin_mawar', 'mawar123', 'Mawar Fitriani', '083145678912', 6, 3),
('petani_adi', 'adi123', 'Adi Triyono', '082245678123', 7, 1),
('produsen_sinta', 'sinta123', 'Sinta Kumalasari', '085334567891', 8, 2),
('admin_agus', 'agus123', 'Agus Hartono', '089612345678', 9, 3),
('petani_rani', 'rani123', 'Rani Ayu Dewi', '087834562311', 10, 1),
('produsen_lilis', 'lilis123', 'Lilis Pratiwi', '082134891234', 11, 2),
('admin_bagus', 'bagus123', 'Bagus Wibisono', '081355662211', 12, 3),
('petani_nanda', 'nanda123', 'Nanda Rahmawati', '081244718236', 13, 1),
('produsen_seno', 'seno123', 'Seno Dwi Kurniawan', '089611238737', 14, 2),
('admin_dwi', 'dwi123', 'Dwi Sulistyo', '083142312457', 15, 3);

INSERT INTO kategori_benih(id_kategori_benih, nama_kategori) VALUES
(1, 'Padi'),
(2, 'Jagung'),
(3, 'Cabai'),
(4, 'Sayuran');

INSERT INTO benih (nama_benih, harga, id_kategori_benih, id_user) 
VALUES
-- kategori 1 (padi)
('Padi IR64', 50000, 1, 2),
('Padi Inpari 30', 55000, 1, 5),
('Padi Mekongga', 60000, 1, 8),

-- kategori 2 (jagung)
('Jagung Bisi-2', 45000, 2, 2),
('Jagung Pioneer P32', 70000, 2, 11),
('Jagung NK212', 65000, 2, 14),

-- kategori 3 (cabai)
('Cabai Rawit Lokal', 30000, 3, 5),
('Cabai Besar TM 99', 35000, 3, 2),
('Cabai Lado F1', 38000, 3, 8),
('Cabai Arimbi', 36000, 3, 11),

-- kategori 4 (sayuran)
('Selada Hijau', 20000, 4, 14),
('Bayam Merah', 18000, 4, 2),
('Kangkung Darat', 15000, 4, 5),
('Sawi Putih', 22000, 4, 8),
('Tomat Lokal', 25000, 4, 11);

INSERT INTO riwayat_produksi (tanggal_produksi, tanggal_kadaluarsa, jumlah_produksi, id_benih)
VALUES
('2025-01-20', '2026-01-20', 500, 1),
('2025-01-25', '2026-01-25', 300, 2),
('2025-01-30', '2026-01-30', 200, 3),
('2025-04-09', '2026-04-09', 600, 2),
('2025-05-23', '2026-05-23', 700, 5),
('2025-06-18', '2026-06-18', 550, 7),
('2025-07-30', '2026-07-30', 420, 8),
('2025-08-14', '2026-08-14', 900, 6),
('2025-09-22', '2026-09-22', 680, 9),
('2025-10-11', '2026-10-11', 750, 10),
('2025-01-19', '2026-01-19', 350, 11),
('2025-02-02', '2026-02-02', 420, 12),
('2025-02-12', '2026-02-12', 510, 13),
('2025-02-25', '2026-02-25', 610, 14),
('2025-03-04', '2026-03-04', 470, 15);

INSERT INTO kabupaten (nama) VALUES
('Jember');

INSERT INTO kecamatan (nama, id_kabupaten) VALUES
('Patrang', 1),
('Sumbersari', 1),
('Kaliwates', 1),
('Arjasa', 1),
('Ajung', 1),
('Rambipuji', 1),
('Balung', 1),
('Wuluhan', 1),
('Puger', 1),
('Ambulu', 1);

INSERT INTO desa (nama, id_kecamatan) VALUES
-- 1. Patrang
('Patrang', 1),
('Jember Lor', 1),
('Slawu', 1),

-- 2. Sumbersari
('Sumbersari', 2),
('Tegal Besar', 2),
('Kebonsari', 2),

-- 3. Kaliwates
('Kaliwates', 3),
('Mangli', 3),
('Kebonagung', 3),

-- 4. Arjasa
('Arjasa', 4),
('Kemuning Lor', 4),
('Darsono', 4),

-- 5. Ajung
('Ajung', 5),
('Pancakarya', 5),
('Sabri', 5),

-- 6. Rambipuji
('Rambipuji', 6),
('Curah Malang', 6),
('Rambigundam', 6),

-- 7. Balung
('Balung Kulon', 7),
('Balung Lor', 7),
('Gumelar', 7),

-- 8. Wuluhan
('Wuluhan', 8),
('Tamansari', 8),
('Lojejer', 8),

-- 9. Puger
('Puger Kulon', 9),
('Puger Wetan', 9),
('Mlokorejo', 9),

-- 10. Ambulu
('Ambulu', 10),
('Pontang', 10),
('Sabrang', 10);
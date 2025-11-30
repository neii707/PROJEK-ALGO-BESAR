CREATE TYPE enum_transaksi AS ENUM('dikemas', 'dikirim', 'diterima', 'selesai');
CREATE TYPE enum_pembayaran AS ENUM ('tunai', 'non tunai');
CREATE TYPE enum_role AS ENUM ('petani', 'produsen', 'admin');

CREATE table kategori_benih(
id_kategori_benih serial primary key,
nama_kategori Varchar(64) not null
);

CREATE TABLE users(
id_user SERIAL PRIMARY KEY,
username VARCHAR(32) UNIQUE NOT NULL,
password VARCHAR(32) UNIQUE NOT NULL,
nama VARCHAR(20) NOT NULL,
no_telp VARCHAR(15) NOT NULL,
role enum_role NOT NULL
);

ALTER TABLE users
ADD COLUMN id_desa INTEGER;

ALTER TABLE users
ADD CONSTRAINT fk_user_desa
FOREIGN KEY (id_desa)
REFERENCES desa(id_desa)
ON DELETE SET NULL;

CREATE TABLE benih(
id_benih SERIAL PRIMARY KEY,
nama_benih VARCHAR(32) NOT NULL,
harga INTEGER NOT NULL,

id_kategori_benih INTEGER REFERENCES kategori_benih(id_kategori_benih)
);

ALTER TABLE users
ADD COLUMN detail_alamat VARCHAR(64);

CREATE TABLE pesanan(
id_pesanan SERIAL PRIMARY KEY,
tanggal_pesanan DATE NOT NULL,

id_user INTEGER REFERENCES users(id_user)
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
nama varchar(32) NOT NULL
);

create table kecamatan(
id_kecamatan serial primary key,
nama varchar(64) NOT NULL,

id_kabupaten integer references kabupaten(id_kabupaten)
);

create table desa(
id_desa serial primary key,
nama varchar(64) NOT NULL,

id_kecamatan integer references kecamatan(id_kecamatan)
);

INSERT INTO users(username, password, nama, no_telp, role, detail_alamat) VALUES
('petani_andi', 'andi123', 'Andi Santoso', '081234567890', 'petani', 'Jl. Mawar No. 12'),
('produsen_budi', 'budi123', 'Budi Prasetyo', '082345678901', 'produsen', 'Jl. Semeru No. 44'),
('admin_sri', 'sri123', 'Sri Lestari', '083456789012', 'admin', 'Jl. Kartini No. 9'),
('petani_joko', 'joko123', 'Joko Susanto', '082376244616', 'petani', 'Jl. Kenanga No. 21'),
('produsen_eko', 'eko123', 'Eko Saputra', '082134567812', 'produsen', 'Jl. Ahmad Yani No. 33'),
('admin_mawar', 'mawar123', 'Mawar Fitriani', '083145678912', 'admin', 'Jl. Diponegoro No. 7'),
('petani_adi', 'adi123', 'Adi Triyono', '082245678123', 'petani', 'Jl. Letjen Suprapto No. 15'),
('produsen_sinta', 'sinta123', 'Sinta Kumalasari', '085334567891', 'produsen', 'Jl. Cempaka No. 56'),
('admin_agus', 'agus123', 'Agus Hartono', '089612345678', 'admin', 'Jl. Trunojoyo No. 18'),
('petani_rani', 'rani123', 'Rani Ayu Dewi', '087834562311', 'petani', 'Jl. Patimura No. 24'),
('produsen_lilis', 'lilis123', 'Lilis Pratiwi', '082134891234', 'produsen', 'Jl. S. Parman No. 80'),
('admin_bagus', 'bagus123', 'Bagus Wibisono', '081355662211', 'admin', 'Jl. Sultan Agung No. 5'),
('petani_nanda', 'nanda123', 'Nanda Rahmawati', '081244718236', 'petani', 'Jl. Melati No. 29'),
('produsen_seno', 'seno123', 'Seno Dwi Kurniawan', '089611238737', 'produsen', 'Jl. Riau No. 91'),
('admin_dwi', 'dwi123', 'Dwi Sulistyo', '083142312457', 'admin', 'Jl. Gatot Subroto No. 3');

INSERT INTO kategori_benih(nama_kategori) VALUES
('Padi'),
('Jagung'),
('Cabai'),
('Sayuran');

INSERT INTO benih(nama_benih, harga, id_kategori_benih) 
VALUES
-- kategori 1 (padi)
('Padi IR64', 50000, 1),
('Padi Inpari 30', 55000, 1),
('Padi Mekongga', 60000, 1),

-- kategori 2 (jagung)
('Jagung Bisi-2', 45000, 2),
('Jagung Pioneer P32', 70000, 2),
('Jagung NK212', 65000, 2),

-- kategori 3 (cabai)
('Cabai Rawit Lokal', 30000, 3),
('Cabai Besar TM 99', 35000, 3),
('Cabai Lado F1', 38000, 3),
('Cabai Arimbi', 36000, 3),

-- kategori 4 (sayuran)
('Selada Hijau', 20000, 4),
('Bayam Merah', 18000, 4),
('Kangkung Darat', 15000, 4),
('Sawi Putih', 22000, 4),
('Tomat Lokal',  25000, 4);

INSERT INTO riwayat_produksi(tanggal_produksi, tanggal_kadaluarsa, jumlah_produksi, id_benih)
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


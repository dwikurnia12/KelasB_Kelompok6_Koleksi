# Sistem Manajemen Koleksi Perpustakaan Berbasis SOLID

## Deskripsi Proyek
Program merupakan implementasi konsep Pemrograman Berbasis Objek (PBO) beserta prinsip SOLID pada sistem pengelolaan koleksi perpustakaan.

Sistem mampu mengelola berbagai jenis koleksi seperti:
- Buku
- Majalah
- Jurnal

Fitur yang tersedia yaitu:
1. Menambah koleksi
2. Menghapus koleksi
3. Melihat seluruh koleksi

## Pembagian Tugas

| Nama | NIM | Tugas |
|--------|--------|--------|
| Diah Anggraeni | K3525055 | Membuat class koleksi_interfaces.py |
| Febriana Putri Q | K3525007| Mengimplementasikan class buku.py dan jurnal.py |
| Queennera Martha K W| K3525012 | Mengimplementasikan abstrac class koleksi.py dan majalah.py |
| Arofa Karindra B| K3525051 | Mengimplementasikan koleksi_factory.py dan koleksi_manager.py |
| Dwi Kurniawati H| K3525056 | Mengimplementasikan main.py |

## Struktur Repository

koleksi/
│
├── interfaces/
│   ├── __init__.py
│   └── koleksi_interfaces.py
│
├── models/
│   ├── __init__.py
│   ├── koleksi.py
│   ├── buku.py
│   ├── majalah.py
│   └── jurnal.py
│
├── services/
│   ├── __init__.py
│   ├── koleksi_factory.py
│   └── koleksi_manager.py
│
├── main.py
└── README.md

## Contoh Output

---------------------------
Menu Koleksi
---------------------------
1. Tambah Koleksi
2. Hapus Koleksi
3. Tampilkan Semua Koleksi
4. Keluar



from abc import ABC, abstractmethod


class Koleksi(ABC):
    def __init__(self, jenis, kode_koleksi, judul, tahun_terbit, penerbit):
        self.jenis = jenis
        self.kode_koleksi = kode_koleksi
        self.judul = judul
        self.tahun_terbit = tahun_terbit
        self.penerbit = penerbit

    @abstractmethod
    def tampil_data(self, nomor):
        """Method abstrak yang WAJIB di-override oleh class turunan"""
        pass



class Buku(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, pengarang, penerbit):
        super().__init__("Buku", kode_koleksi, judul, tahun_terbit, penerbit)
        self.pengarang = pengarang

    def tampil_data(self, nomor):
        print(f"Koleksi {nomor}:")
        print(f"Jenis         : {self.jenis}")
        print(f"Kode Koleksi  : {self.kode_koleksi}")
        print(f"Judul         : {self.judul}")
        print(f"Thn Terbit    : {self.tahun_terbit}")
        print(f"Pengarang     : {self.pengarang}")
        print(f"Penerbit      : {self.penerbit}")


class Majalah(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, edisi):
        super().__init__("Majalah", kode_koleksi, judul, tahun_terbit, penerbit)
        self.edisi = edisi

    def tampil_data(self, nomor):
        print(f"Koleksi {nomor}:")
        print(f"Jenis         : {self.jenis}")
        print(f"Kode Koleksi  : {self.kode_koleksi}")
        print(f"Judul         : {self.judul}")
        print(f"Tahun Terbit  : {self.tahun_terbit}")
        print(f"Penerbit      : {self.penerbit}")
        print(f"Edisi         : {self.edisi}")


class Jurnal(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, bidang_studi, impact_factor):
        super().__init__("Jurnal", kode_koleksi, judul, tahun_terbit, penerbit)
        self.bidang_studi = bidang_studi
        self.impact_factor = impact_factor

    def tampil_data(self, nomor):
        print(f"Koleksi {nomor}:")
        print(f"Jenis         : {self.jenis}")
        print(f"Kode Koleksi  : {self.kode_koleksi}")
        print(f"Judul         : {self.judul}")
        print(f"Thn Terbit    : {self.tahun_terbit}")
        print(f"Penerbit      : {self.penerbit}")
        print(f"Impact Factor : {self.impact_factor}")
        print(f"Bidang Studi  : {self.bidang_studi}")


class DVDFilm(Koleksi):
    def __init__(self, kode_koleksi, judul, tahun_terbit, bidang_ilmu, durasi):
        # DVD Film Dokumenter tidak memiliki penerbit di lembar soal, set default "-"
        super().__init__("DVD Film Dokumenter", kode_koleksi, judul, tahun_terbit, "-")
        self.bidang_ilmu = bidang_ilmu
        self.durasi = durasi

    def tampil_data(self, nomor):
        print(f"Koleksi {nomor}:")
        print(f"Jenis         : {self.jenis}")
        print(f"Kode Koleksi  : {self.kode_koleksi}")
        print(f"Judul         : {self.judul}")
        print(f"Tahun         : {self.tahun_terbit}")
        print(f"Bidang Ilmu   : {self.bidang_ilmu}")
        print(f"Durasi        : {self.durasi}")
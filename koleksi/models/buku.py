from models.koleksi import Koleksi

class Buku(Koleksi):

    def __init__(self, kode, judul, tahun,
                 pengarang, penerbit):
        super().__init__(kode, judul, tahun)

        self.pengarang = pengarang
        self.penerbit = penerbit

    def tampil(self):
        print("Jenis : Buku")
        print("Kode :", self.kode)
        print("Judul :", self.judul)
        print("Tahun :", self.tahun)
        print("Pengarang :", self.pengarang)
        print("Penerbit :", self.penerbit)
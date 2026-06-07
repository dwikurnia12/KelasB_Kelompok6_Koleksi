from models.koleksi import Koleksi

class Buku(Koleksi):

    def __init__(self, kode_koleksi, judul, tahun_terbit, pengarang, penerbit):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)

        self._pengarang = pengarang

    def tampilkan_info(self):
        print("Jenis : Buku")
        print("Kode :", self._kode_koleksi)
        print("Judul :", self._judul)
        print("Tahun :", self._tahun_terbit)
        print("Pengarang :", self._pengarang)
        print("Penerbit :", self._penerbit)
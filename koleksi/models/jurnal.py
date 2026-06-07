from models.koleksi import Koleksi

class Jurnal(Koleksi):

    def __init__(self, kode_koleksi, judul, tahun_terbit, penerbit, bidang_studi, impact_factor):

        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)

        self._bidang_studi = bidang_studi
        self._impact_factor = impact_factor

    def tampilkan_info(self):
        print("Jenis : Jurnal")
        print("Kode :", self._kode_koleksi)
        print("Judul :", self._judul)
        print("Tahun :", self._tahun_terbit)
        print("Penerbit :", self._penerbit)
        print("Bidang :", self._bidang_studi)
        print("Impact Factor :", self._impact_factor)
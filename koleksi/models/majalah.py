from models.koleksi import Koleksi

class Majalah(Koleksi):

    def __init__(self, kode_koleksi: str, judul: str, tahun_terbit: str, penerbit: str, edisi: str):
        super().__init__(kode_koleksi, judul, tahun_terbit, penerbit)
        self._edisi = edisi

    def tampilkan_info(self) -> None:

        print(f"Jenis          : Majalah")
        print(f"Kode Koleksi   : {self._kode_koleksi}")
        print(f"Judul          : {self._judul}")
        print(f"Tahun Terbit     : {self._tahun_terbit}")
        print(f"Penerbit       : {self._penerbit}")
        print(f"Edisi          : {self._edisi}")

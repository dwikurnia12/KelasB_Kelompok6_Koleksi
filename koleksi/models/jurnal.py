from models.koleksi import Koleksi

class Jurnal(Koleksi):

    def __init__(self, kode, judul,
                 tahun, penerbit,
                 bidang, impact):

        super().__init__(kode, judul, tahun)

        self.penerbit = penerbit
        self.bidang = bidang
        self.impact = impact

    def tampil(self):
        print("Jenis : Jurnal")
        print("Kode :", self.kode)
        print("Judul :", self.judul)
        print("Tahun :", self.tahun)
        print("Penerbit :", self.penerbit)
        print("Bidang :", self.bidang)
        print("Impact Factor :", self.impact)
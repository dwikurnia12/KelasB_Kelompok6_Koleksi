from models.buku import Buku
from models.majalah import Majalah
from models.jurnal import Jurnal

class KoleksiFactory:
    @staticmethod
    def create_koleksi(jenis, **kwargs):
        if jenis == "1":
            return Buku(
                kode_koleksi=kwargs.get('kode'),
                judul=kwargs.get('judul'),
                tahun_terbit=kwargs.get('tahun'),
                pengarang=kwargs.get('pengarang'),
                penerbit=kwargs.get('penerbit')
            )
        elif jenis == "2":
            return Majalah(
                kode_koleksi=kwargs.get('kode'),
                judul=kwargs.get('judul'),
                tahun_terbit=kwargs.get('tahun'),
                penerbit=kwargs.get('penerbit'),
                edisi=kwargs.get('edisi')
            )
        elif jenis == "3":
            return Jurnal(
                kode_koleksi=kwargs.get('kode'),
                judul=kwargs.get('judul'),
                tahun_terbit=kwargs.get('tahun'),
                penerbit=kwargs.get('penerbit'),
                bidang_studi=kwargs.get('bidang'),
                impact_factor=kwargs.get('impact')
            )
        else:
            raise ValueError("Jenis koleksi tidak valid")

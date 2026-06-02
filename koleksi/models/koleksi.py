from abc import abstractmethod
from koleksi.interfaces.koleksi_interfaces import KoleksiInterface


class Koleksi(KoleksiInterface):

    def __init__(self, kode_koleksi: str, judul: str, tahun_terbit: str, penerbit: str):
        self._kode_koleksi = kode_koleksi
        self._judul = judul
        self._tahun_terbit = tahun_terbit
        self._penerbit = penerbit

    def get_kode(self) -> str:
        return self._kode_koleksi

    @abstractmethod
    def tampilkan_info(self) -> None:
       
        pass

class KoleksiManager:
    def __init__(self):
        self._daftar_koleksi = []

    def tambah_koleksi(self, objek_koleksi):
        if objek_koleksi is not None:
            self._daftar_koleksi.append(objek_koleksi)
            print("[SUKSES] Koleksi berhasil disimpan!")
        else:
            print("[GAGAL] Objek koleksi kosong.")

    def hapus_koleksi(self, kode):
        for item in self._daftar_koleksi:
            if item.get_kode() == kode:
                self._daftar_koleksi.remove(item)
                print(f"\n[SUKSES] Koleksi dengan kode '{kode}' berhasil dihapus.")
                return True
        print(f"\n[GAGAL] Koleksi dengan kode '{kode}' tidak ditemukan.")
        return False

    def tampilkan_semua(self):
        if not self._daftar_koleksi:
            print("Belum ada koleksi yang tersimpan.")
            return

        print("========================")
        print("  DAFTAR SEMUA KOLEKSI  ")
        print("========================")
        for item in self._daftar_koleksi:
            item.tampilkan_info()
            print("-" * 24)
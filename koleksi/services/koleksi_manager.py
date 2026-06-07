class KoleksiManager:
    def __init__(self):
        self.koleksi_list = []

    def tambah_koleksi(self, objek_koleksi):
        self.koleksi_list.append(objek_koleksi)
        
    def hapus_koleksi(self, kode):
        for item in self.koleksi_list:
            if item.get_kode() == kode:
                self.koleksi_list.remove(item)
                print("Hapus data koleksi sukses")
                return True
            print("Kode koleksi tidak ditemukan")
            return False
    
    def tampilkan_info(self):

        if not self.koleksi_list:
            print("Tidak ada data koleksi.")
            return
        
        for item in self.koleksi_list:
            item.tampilkan_info()
            print("-" * 30)
    


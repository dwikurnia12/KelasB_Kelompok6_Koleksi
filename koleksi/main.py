from services.koleksi_manager import KoleksiManager
from services.koleksi_factory import KoleksiFactory

def tambah_data(manager):
    print("--------------------")
    print("Tambah Koleksi")
    print("--------------------")
    print("1. Buku")
    print("2. Majalah")
    print("3. Jurnal")
    
    jenis = input("Pilih jenis koleksi : ")
    
    kode = input("Kode koleksi : ")
    judul = input("Judul        : ")
    tahun = input("Tahun terbit : ")
    penerbit = input("Penerbit     : ")
    
    data = {
        "kode": kode,
        "judul": judul,
        "tahun": year if 'year' in locals() else tahun,
        "penerbit": penerbit
    }
    
    if jenis == "1":
        data["pengarang"] = input("Pengarang    : ")
    elif jenis == "2":
        data["edisi"] = input("Edisi        : ")
    elif jenis == "3":
        data["bidang"] = input("Bidang Studi : ")
        data["impact"] = input("Impact Factor: ")
    else:
        print("Jenis koleksi tidak valid!")
        return

    try:
        objek_jadi = KoleksiFactory.create_koleksi(jenis, **data)
        manager.tambah_koleksi(objek_koleksi=objek_jadi)
    except ValueError as e:
        print(f"\nGagal membuat objek: {e}")


def hapus_data(manager):
    print("--------------------")
    print("Hapus Koleksi")
    print("--------------------")
    kode = input("Masukkan kode koleksi yang ingin dihapus: ")
    manager.hapus_koleksi(kode)


def main():
    manager = KoleksiManager()
    
    while True:
        print("\n====================")
        print("MENU DATA KOLEKSI")
        print("====================")
        print("1. Tambah Koleksi")
        print("2. Hapus Koleksi")
        print("3. Tampilkan Semua Koleksi")
        print("4. Keluar")
        
        pilihan = input("Pilihan menu : ")
        print()
        
        if pilihan == "1":
            tambah_data(manager)
        elif pilihan == "2":
            hapus_data(manager)
        elif pilihan == "3":
            manager.tampilkan_semua()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan menu tidak tersedia!")

if __name__ == "__main__":
    main()
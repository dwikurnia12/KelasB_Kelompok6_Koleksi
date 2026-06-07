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

    kode = input("Kode koleksi  : ")
    judul = input("Judul         : ")
    tahun = input("Tahun terbit  : ")
    penerbit = input("Penerbit      : ")

    data = {
        "kode": kode,
        "judul": judul,
        "tahun": tahun,
        "penerbit": penerbit
    }

    if jenis == "1":
        data["pengarang"] = input("Pengarang : ")

    elif jenis == "2":
        data["edisi"] = input("Edisi : ")

    elif jenis == "3":
        data["bidang"] = input("Bidang studi : ")
        data["impact"] = input("Impact factor : ")

    else:
        print("Jenis koleksi tidak valid")
        return

    try:
        koleksi = KoleksiFactory.create_koleksi(jenis, **data)
        manager.tambah_koleksi(koleksi)
        print("Data koleksi berhasil ditambahkan")

    except ValueError as e:
        print(e)


def hapus_data(manager):
    print("--------------------")
    print("Hapus Koleksi")
    print("--------------------")

    kode = input("Masukkan kode koleksi : ")
    manager.hapus_koleksi(kode)


def tampil_data(manager):
    manager.tampilkan_info()


def main():
    manager = KoleksiManager()

    while True:
        print("\n===========================")
        print("MENU DATA KOLEKSI")
        print("===========================")
        print("1. Tambah Koleksi")
        print("2. Hapus Koleksi")
        print("3. Tampilkan Semua Koleksi")
        print("4. Keluar")

        pilihan = input("Pilihan menu : ")
        print("DEBUG:", repr(pilihan))

        if pilihan == "1":
            tambah_data(manager)

        elif pilihan == "2":
            hapus_data(manager)

        elif pilihan == "3":
            tampil_data(manager)

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia")


if __name__ == "__main__":
    main()
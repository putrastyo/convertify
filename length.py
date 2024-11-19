satuan_panjang = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
isi_data = {}

def konversi_ke_meter(nilai, satuan_asal):
    if satuan_asal == "mm":
        return nilai / 1000
    if satuan_asal == "cm":
        return nilai / 100
    elif satuan_asal == "dm":
        return nilai / 10
    elif satuan_asal == "m":
        return nilai
    elif satuan_asal == "dam":
        return nilai * 10
    elif satuan_asal == "hm":
        return nilai * 100
    elif satuan_asal == "km":
        return nilai * 1000

def konversi_dari_meter(nilai, satuan_tujuan):
    if satuan_tujuan == "mm":
        return nilai * 1000
    if satuan_tujuan == "cm":
        return nilai * 100
    elif satuan_tujuan == "dm":
        return nilai * 10
    elif satuan_tujuan == "m":
        return nilai
    elif satuan_tujuan == "dam":
        return nilai / 10
    elif satuan_tujuan == "hm":
        return nilai / 100
    elif satuan_tujuan == "km":
        return nilai / 1000

def tampilkan_data():
    if not isi_data:
        print("Data kosong.")
    else:
        print("\n Data Panjang Yang Tersedia:")
        for nama, (nilai, satuan) in isi_data.items():
            print(f"{nama}: {nilai} {satuan}")

def tambah_panjang(nama, nilai, satuan):
    if nama in isi_data:
        print("Data sudah ada. Gunakan nama yang berbeda.")
    elif satuan not in satuan_panjang:
        print("Satuan panjang tidak valid.")
    else:
        isi_data[nama] = (nilai, satuan)
        print(f"Data Panjang '{nama}' berhasil ditambahkan.")
        simpan_txt()

def hapus_panjang(nama):
    if nama not in isi_data:
        print("Data Tidak Ditemukan.")
    else:
        del isi_data[nama]
        print(f"Data Panjang '{nama}' berhasil dihapus.")
        simpan_txt()

def update_panjang(nama, nilai_baru, satuan_baru):
    if nama not in isi_data:
        print("Data Tidak Ditemukan.")
    elif satuan_baru not in satuan_panjang:
        print("Satuan panjang tidak valid.")
    else:
        isi_data[nama] = (nilai_baru, satuan_baru)
        print(f"\n Panjang '{nama}' berhasil diupdate menjadi {nilai_baru} {satuan_baru}.\n")
        simpan_txt()

def simpan_txt():
    with open("length.txt", "w") as file:
        for nama, (nilai, satuan) in isi_data.items():
            file.write(f"{nama}: {nilai} {satuan}\n")
    print("\n Data Berhasil Disimpan.")

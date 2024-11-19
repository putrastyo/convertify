satuan_suhu = ["Celsius", "Reamur", "Fahrenheit", "Kelvin"]
riwayat_suhu = {}
riwayat_konversi = []


def konversi_ke_celcius(nilai, satuan):
    if satuan == "Celsius":
        return nilai
    elif satuan == "Reamur":
        return nilai * 5 / 4
    elif satuan == "Fahrenheit":
        return (nilai - 32) * 5 / 9
    elif satuan == "Kelvin":
        return nilai - 273.15


def konversi_dari_celcius(nilai, satuan):
    if satuan == "Celsius":
        return nilai
    elif satuan == "Reamur":
        return nilai * 4 / 5
    elif satuan == "Fahrenheit":
        return (nilai * 9 / 5) + 32
    elif satuan == "Kelvin":
        return nilai + 273.15


def cari_indeks(satuan):
    if satuan in satuan_suhu:
        return satuan_suhu.index(satuan)
    else:
        return -1


def urutkan_satuan():
    return sorted(satuan_suhu)


def tampilkan_riwayat():
    if not riwayat_suhu and not riwayat_konversi:
        print("Riwayat suhu kosong.")
    else:
        print("\nRiwayat suhu tersimpan:")
        for nama, (nilai, satuan) in riwayat_suhu.items():
            print(f"{nama}: {nilai} {satuan}")
        print("\nRiwayat konversi suhu:")
        for item in riwayat_konversi:
            print(item)

def tambah_suhu(nama, nilai, satuan):
    if nama in riwayat_suhu:
        print("Nama suhu sudah ada. Gunakan nama yang berbeda.")
    elif satuan not in satuan_suhu:
        print("Satuan tidak valid.")
    else:
        riwayat_suhu[nama] = (nilai, satuan)
        print(f"Suhu '{nama}' berhasil ditambahkan.")
        simpan_ke_file()

def ubah_suhu(nama, nilai, satuan):
    if nama not in riwayat_suhu:
        print("Nama suhu tidak ditemukan.")
    elif satuan not in satuan_suhu:
        print("Satuan tidak valid.")
    else:
        riwayat_suhu[nama] = (nilai, satuan)
        print(f"Suhu '{nama}' berhasil diubah.")
        simpan_ke_file()

def hapus_suhu(nama):
    if nama not in riwayat_suhu:
        print("Nama suhu tidak ditemukan.")
    else:
        del riwayat_suhu[nama]
        print(f"Suhu '{nama}' berhasil dihapus.")
        simpan_ke_file()

def simpan_ke_file():
    with open("temperature.txt", "w") as file:
        for nama, (nilai, satuan) in riwayat_suhu.items():
            file.write(f"{nama}: {nilai} {satuan}\n")
    print(f"Data {nama} dengan {nilai} {satuan} telah disimpan")

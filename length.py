# Daftar satuan panjang
satuan_panjang = ["km", "hm", "dam", "m", "dm", "cm", "mm"]

# Fungsi untuk mengonversi ke meter
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

# Fungsi untuk mengonversi dari meter
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

# Fungsi untuk mencari indeks satuan dalam daftar satuan panjang
def cari_indeks_panjang(satuan):
    if satuan in satuan_panjang:
        return satuan_panjang.index(satuan)
    else:
        return -1

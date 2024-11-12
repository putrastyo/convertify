satuan_suhu = ["Celsius", "Reamur", "Fahrenheit", "Kelvin"]


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

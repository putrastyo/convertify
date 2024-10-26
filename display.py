def display_units(units):
    print('Daftar satuan:')
    for key, unit in units.items():
        print(f"{key}. {unit['name']} ({unit['alias']})")

    print("--- masukkan salah satu angka diatas ----")
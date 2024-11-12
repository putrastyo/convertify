from currency import get_currencies, operasi_mata_uang
from temperature import urutkan_satuan, cari_indeks,konversi_ke_celcius, konversi_dari_celcius
from display import display_units

print('''
1. Mata uang
2. Suhu
3. Panjang
4. (keluar aplikasi)
''')

while True:
    operasi = int(input('Operasi nomor berapa yang anda pilih? (1, 2, atau 3): '))

    if operasi < 0 or operasi > 4:
        print('Operasi tidak valid.')
    elif operasi == 1:
        print("=============")
        print("Anda memilih: MATA UANG")
        print("=============")
        print("")

        # 1. Masukkan nominal
        nominal = int(input('Masukkan nominal ---> '))
        # 2. dapetin satuan-satuannya
        currencies = get_currencies()
        # 3. tampilin satuan-sataunnya
        display_units(currencies)
        # 4. Pilih mau ubah dari mana ke mana
        from_unit = int(input("ubah dari: "))
        to_unit = int(input("menjadi: "))
        # 5. hasilkan
        result = operasi_mata_uang(nominal, from_unit, to_unit, currencies)
        print(f"{currencies[to_unit]['name']} {result}")
    elif operasi == 2:
        print("=============")
        print("Anda memilih: SUHU")
        print("=============")
        print("")

        print("Daftar satuan suhu yang tersedia:", urutkan_satuan())
        satuan_input = input("Masukkan satuan suhu input (Celsius/Reamur/Fahrenheit/Kelvin): ")

        if cari_indeks(satuan_input) is None:
            print("Satuan suhu tidak valid.")
        else:
            nilai = float(input(f"Masukkan nilai suhu dalam {satuan_input}: "))
            satuan_output = input("Masukkan satuan suhu output (Celsius/Reamur/Fahrenheit/Kelvin): ")

            if cari_indeks(satuan_output) is None:
                print("Satuan suhu tidak valid.")
            else:
                nilai_celcius = konversi_ke_celcius(nilai, satuan_input)
                if nilai_celcius is None:
                    print("Kesalahan pada konversi ke Celcius.")
                else:
                    nilai_akhir = konversi_dari_celcius(nilai_celcius, satuan_output)
                    if nilai_akhir is None:
                        print("Kesalahan pada konversi dari Celcius ke satuan output.")
                    else:
                        print(f"{nilai} {satuan_input} setara dengan {nilai_akhir:.1f} {satuan_output}")
    elif operasi == 3:
        pass
    elif operasi == 4:
        print("=============================")
        print("Terimakasih dan Sampai Jumpa!")
        print("=============================")
        break

    print("")
    print("==================================")
    print("")





















from currency import *
from temperature import *
from length import *
from display import display_units

while True:
    print("\n -- SELAMAT DATANG DI CONVERTIFY --")
    print('''
    1. Mata Uang
    2. Suhu
    3. Satuan Panjang
    4. keluar Aplikasi
    ''')
    operasi = int(input('Operasi nomor berapa yang anda pilih? '))

    if operasi < 0 or operasi > 4:
        print('Operasi tidak valid.')
    elif operasi == 1:
        print("=============")
        print("Anda memilih: MATA UANG")
        print("=============")
        print("")

        currencies = read_currencies_from_file()
        if not currencies:
            currencies = get_currencies()
            save_currencies_to_file(currencies)

        while True:
            print("\nCurrency Manager")
            print("1. View Currencies")
            print("2. Add Currency")
            print("3. Update Currency")
            print("4. Delete Currency")
            print("5. Convert")
            print("6. Exit")

            try:
                option = int(input('Masukkan pilihan ---> '))
                if option == 1:
                    display_currencies(currencies)
                elif option == 2:
                    try:
                        currency_id = int(input("Masukkan ID: "))
                        if currency_id in currencies:
                            print("ID sudah ada.")
                            continue
                        name = input("Masukkan nama mata uang: ")
                        alias = input("Masukkan alias: ")
                        in_usd = float(input("Masukkan nilai dalam USD: "))
                        currencies[currency_id] = {'name': name, 'alias': alias, 'in_usd': in_usd}
                        save_currencies_to_file(currencies)
                        print(f"Mata uang '{name}' berhasil ditambahkan.")
                    except ValueError:
                        print("Input tidak valid. Silakan coba lagi.")
                elif option == 3:
                    update_currency(currencies)
                elif option == 4:
                    delete_currency(currencies)
                elif option == 5:
                    try:
                        nominal = float(input('Masukkan nominal ---> '))
                        display_currencies(currencies)
                        from_unit = int(input("Ubah dari (ID): "))
                        to_unit = int(input("Menjadi (ID): "))
                        if from_unit in currencies and to_unit in currencies:
                            result = operasi_mata_uang(nominal, from_unit, to_unit, currencies)
                            print(f"{currencies[to_unit]['name']} {result:.2f}")
                        else:
                            print("ID mata uang tidak valid.")
                    except ValueError:
                        print("Input tidak valid. Silakan coba lagi.")
                elif option == 6:
                    print("Goodbye!")
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih antara 1-6.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")

    elif operasi == 2:
        satuan_suhu = ["Celsius", "Reamur", "Fahrenheit", "Kelvin"]
        riwayat_suhu = {}
        riwayat_konversi = []

        # Program utama
        print("Daftar satuan suhu yang tersedia:", urutkan_satuan())
        while True:
            print("\nMenu:")
            print("1. Tambah daftar suhu ke riwayat")
            print("2. Lihat riwayat suhu")
            print("3. Ubah suhu di riwayat")
            print("4. Hapus suhu dari riwayat")
            print("5. Konversi suhu")
            print("0. Keluar")
            
            pilihan = input("Pilih menu (1/2/3/4/5/0): ")
            
            if pilihan == "1":
                nama = input("Masukkan nama suhu (ex: suhu ruangan): ").lower()
                nilai = float(input("Masukkan nilai suhxu: "))
                satuan = input("Masukkan satuan suhu (Celsius/Reamur/Fahrenheit/Kelvin): ")
                tambah_suhu(nama, nilai, satuan)
            elif pilihan == "2":
                tampilkan_riwayat()
            elif pilihan == "3":
                nama = input("Masukkan nama suhu yang ingin diubah: ").lower()
                nilai = float(input("Masukkan nilai baru: "))
                satuan = input("Masukkan satuan baru (Celsius/Reamur/Fahrenheit/Kelvin): ")
                ubah_suhu(nama, nilai, satuan)
            elif pilihan == "4":
                nama = input("Masukkan nama suhu yang ingin dihapus: ")
                hapus_suhu(nama)
            elif pilihan == "5":
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
                        nilai_akhir = konversi_dari_celcius(nilai_celcius, satuan_output)
                        hasil_konversi = f"{nilai} {satuan_input} -> {nilai_akhir:.1f} {satuan_output}"
                        riwayat_konversi.append(hasil_konversi)
                        print(hasil_konversi)
            elif pilihan == "0":
                print("Keluar dari program.")
                break
            else:
                print("Pilihan tidak valid.")


    elif operasi == 3:
        satuan_panjang = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
        isi_data = {}

        while True:
            print("\nMenu:")
            print("1. Konversi Satuan Panjang")
            print("2. Lihat Data")
            print("3. Tambah Data")
            print("4. Update Data")
            print("5. Hapus Data")
            print("6. Urutkan Data")
            print("0. Keluar")
            
            pilihan = input("Pilih menu (1/2/3/4/5/6/0): ")
            
            if pilihan == '1':
                satuan_input = input("Masukkan satuan panjang input (km/hm/dam/m/dm/cm/mm): ").lower()
                
                if satuan_input not in satuan_panjang:
                    print("Satuan panjang tidak valid.")
                    continue
                
                nilai = float(input(f"Masukkan nilai panjang dalam {satuan_input}: "))
                
                satuan_output = input("Masukkan satuan panjang output (km/hm/dam/m/dm/cm/mm): ").lower()
                
                if satuan_output not in satuan_panjang:
                    print("Satuan panjang tidak valid.")
                    continue
                
                nilai_meter = konversi_ke_meter(nilai, satuan_input)
                nilai_akhir = konversi_dari_meter(nilai_meter, satuan_output)
                
                hasil_konversi = f"{nilai} {satuan_input} setara dengan {nilai_akhir} {satuan_output}"
                print(hasil_konversi)
            
            elif pilihan == '2':
                tampilkan_data()
            
            elif pilihan == '3':
                nama = input("Masukkan nama panjang: ").lower()
                nilai = float(input("Masukkan nilai panjang: "))
                satuan = input("Masukkan Satuan Panjangnya (km/hm/dam/m/dm/cm/mm): ").lower()
                tambah_panjang(nama, nilai, satuan)
            
            elif pilihan == '4':
                nama = input("Masukkan nama barang yang ingin diubah: ").lower()
                nilai = float(input("Masukkan nilai baru: "))
                satuan = input("Masukkan satuan baru (km/hm/dam/m/dm/cm/mm): ")
                update_panjang(nama, nilai, satuan)

            elif pilihan == '5':
                nama = input("Masukkan nama panjang yang ingin dihapus: ").lower()
                hapus_panjang(nama)

            elif pilihan == '6':
                if not isi_data:
                    print("Riwayat panjang kosong.")
                else:
                    sorted_riwayat = sorted(isi_data.items())
                    
                    print("\n -- Urutan Data Panjang Barang Berdasarkan Abjad --")
                    for nama, (nilai, satuan) in sorted_riwayat:
                        print(f"{nama}: {nilai} {satuan}")
            
            elif pilihan == '0':
                print("Keluar dari program.")
                break
            
            else:
                print("Pilihan tidak valid.")
                
    elif operasi == 4:
        print("=============================")
        print("Terimakasih dan Sampai Jumpa!")
        print("=============================")
        break

    print()
    print("==================================")
    print()
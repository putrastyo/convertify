from currency import get_currencies, operasi_mata_uang
from temperature import urutkan_satuan, cari_indeks,konversi_ke_celcius, konversi_dari_celcius
from length import konversi_ke_meter, konversi_dari_meter, cari_indeks_panjang
from display import display_units

print('''
1. Mata Uang
2. Suhu
3. Satuan Panjang
4. keluar Aplikasi
''')

while True:
    operasi = int(input('Operasi nomor berapa yang anda pilih? '))

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
        satuan_suhu = ["Celsius", "Reamur", "Fahrenheit", "Kelvin"]
        riwayat_suhu = {}
        riwayat_konversi = []

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
        # Daftar satuan panjang
        satuan_panjang = ["km", "hm", "dam", "m", "dm", "cm", "mm"]
        isi_data = {}

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
                simpan_ke_file()

        def hapus_panjang(nama):
            if nama not in isi_data:
                print("Nama panjang tidak ditemukan.")
            else:
                del isi_data[nama]
                print(f"Data Panjang '{nama}' berhasil dihapus.")
                simpan_ke_file()

        def update_panjang(nama, nilai_baru, satuan_baru):
            if nama not in isi_data:
                print("Nama panjang tidak ditemukan.")
            elif satuan_baru not in satuan_panjang:
                print("Satuan panjang tidak valid.")
            else:
                # Update nilai dan satuan
                isi_data[nama] = (nilai_baru, satuan_baru)
                print(f"\n Panjang '{nama}' berhasil diupdate menjadi {nilai_baru} {satuan_baru}.\n")
                simpan_ke_file()

        def simpan_ke_file():
            with open("length.txt", "w") as file:
                for nama, (nilai, satuan) in isi_data.items():
                    file.write(f"{nama}: {nilai} {satuan}\n")
            print("\n Data Berhasil Disimpan.")

        # Program utama
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
                    # Mengonversi dictionary menjadi list dan mengurutkannya berdasarkan nama
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

    print("")
    print("==================================")
    print("")
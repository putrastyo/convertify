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
        def tampilkan_menu():
            print("=============")
            print("KONVERSI SATUAN PANJANG")
            print("=============")
            print("Menu:")
            print("1. Konversi Panjang")
            print("2. Lihat Panjang Barang")
            print("3. Tambah Panjang")
            print("4. Edit Barang")
            print("5. Urutkan Barang")
            print("6. Hapus Barang")
            print("7. Keluar")
            print("=============")

        def konversi_panjang():
            print("Anda memilih: KONVERSI PANJANG")
            
            satuan_input = input("Masukkan satuan panjang input (km/hm/dam/m/dm/cm/mm): ").lower()
            
            if cari_indeks_panjang(satuan_input) == -1:
                print("Satuan panjang tidak valid.")
                return
            
            nilai = float(input(f"Masukkan nilai panjang dalam {satuan_input}: "))
            satuan_output = input("Masukkan satuan panjang output (km/hm/dam/m/dm/cm/mm): ").lower()
            
            if cari_indeks_panjang(satuan_output) == -1:
                print("Satuan panjang tidak valid.")
                return
            
            nilai_meter = konversi_ke_meter(nilai, satuan_input)
            
            if nilai_meter is None:
                print("Kesalahan pada konversi ke meter.")
                return
            
            nilai_akhir = konversi_dari_meter(nilai_meter, satuan_output)
            
            if nilai_akhir is None:
                print("Kesalahan pada konversi dari meter ke satuan output.")
                return
            
            hasil_konversi = f"{nilai} {satuan_input} setara dengan {nilai_akhir} {satuan_output}"
            print(hasil_konversi)

        def lihat_panjang_barang():
            with open("length.txt", "r") as file:
                data_barang = file.readlines()
                if not data_barang:
                    print("\nTidak ada data barang.\n")
                else:
                    print("\nData Panjang Barang:")
                    for line in data_barang:
                        print(line.strip())

        def tambah_panjang_barang():
            nama_barang = input("Masukkan nama barang: ").lower()
            panjang_barang = input("Masukkan panjang barang (misalnya 10 cm): ")
            
            with open("length.txt", "a") as file:
                file.write(f"{nama_barang}: {panjang_barang}\n")
            
            print(f"Data '{nama_barang}' dengan panjang '{panjang_barang}' berhasil ditambahkan.")

        def hapus_barang():
            lihat_panjang_barang()
            
            nama_barang = input("\n Masukkan nama barang yang ingin dihapus: ").lower()
            
            with open("length.txt", "r") as file:
                data_barang = file.readlines()
            
            with open("length.txt", "w") as file:
                for line in data_barang:
                    if not line.startswith(nama_barang):
                        file.write(line)
                    else:
                        print(f"\nData '{nama_barang}' berhasil dihapus.\n")

        def edit_barang():
            lihat_panjang_barang()
            
            nama_barang = input("\n Masukkan Nama Barang Yang Ingin Diedit: ").lower()
            
            with open("length.txt", "r") as file:
                data_barang = file.readlines()
            
            found = False
            for i in range(len(data_barang)):
                if data_barang[i].startswith(nama_barang):
                    found = True
                    new_value = input(f"Masukkan nilai baru untuk '{nama_barang}': ")
                    data_barang[i] = f"{nama_barang}: {new_value}\n"
                    break
            
            if found:
                with open("length.txt", "w") as file:
                    file.writelines(data_barang)
                print(f"Data '{nama_barang}' berhasil diubah.")
            else:
                print(f"Data '{nama_barang}' tidak ditemukan.")

        def urutkan_barang():
            try:
                with open("length.txt", "r") as file:
                    data_barang = file.readlines()

                # Mengurutkan berdasarkan nama barang
                data_barang.sort(key=lambda x: x.split(':')[0])

                # Menampilkan hasil urutan
                if not data_barang:
                    print("\nTidak ada data barang untuk diurutkan.\n")
                else:
                    print("\nData Panjang Barang setelah diurutkan:")
                    for line in data_barang:
                        print(line.strip())

                # Menyimpan kembali hasil urutan ke dalam file
                with open("length.txt", "w") as file:
                    file.writelines(data_barang)

            except FileNotFoundError:
                print("File length.txt tidak ditemukan.")

        # Program utama
        while True:
            tampilkan_menu()
            
            pilihan = input("Pilih menu: ")
            
            if pilihan == '1':
                konversi_panjang()
            elif pilihan == '2':
                lihat_panjang_barang()
            elif pilihan == '3':
                tambah_panjang_barang()
            elif pilihan == '4':
                edit_barang()
            elif pilihan == '5':
                urutkan_barang()
            elif pilihan == '6':
                hapus_barang()
            elif pilihan == '7':
                print("=============================")
                print("Terimakasih dan Sampai Jumpa!")
                print("=============================")
                exit()
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                
    elif operasi == 4:
        print("=============================")
        print("Terimakasih dan Sampai Jumpa!")
        print("=============================")
        break

    print("")
    print("==================================")
    print("")
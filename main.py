from currency import get_currencies, operasi_mata_uang
from temperature import urutkan_satuan, cari_indeks,konversi_ke_celcius, konversi_dari_celcius, tampilkan_riwayat, tambah_suhu, ubah_suhu, hapus_suhu, simpan_ke_file
from length import konversi_ke_meter, konversi_dari_meter, tampilkan_data, tambah_panjang, update_panjang, hapus_panjang, simpan_txt 
from display import display_units

print("\n -- SELAMAT DATANG DI CONVERTIFY --")
print('''
1. Mata Uang
2. Suhu
3. Satuan Panjang
4. keluar Aplikasi
''')

while True:
    operasi = int(input('Operasi Nomor Berapa Yang Anda Pilih? '))

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

    print("")
    print("==================================")
    print("")
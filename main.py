from currency import get_currencies, operasi_mata_uang
from display import display_units

print('''
1. Mata uang
2. Suhu
3. Panjang
''')

operasi = int(input('Operasi nomor berapa yang anda pilih? (1, 2, atau 3): '))

if operasi < 0 or operasi > 3:
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























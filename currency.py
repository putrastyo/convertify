def get_currencies():
    currencies = {
        1: {
            'name': 'USD',
            'alias': 'Dolar Amerika',
            'in_usd': 1.0
        },
        2: {
            'name': 'EUR',
            'alias': 'Euro',
            'in_usd': 0.85
        },
        3: {
            'name': 'JPY',
            'alias': 'Yen',
            'in_usd': 110.0
        },
        4: {
            'name': 'GBP',
            'alias': 'Pound Sterling',
            'in_usd': 0.75
        },
        5: {
            'name': 'AUD',
            'alias': 'Dolat Australia',
            'in_usd': 1.35
        },
        6: {
            'name': 'IDR',
            'alias': 'Rupiah',
            'in_usd': 15000.0
        }
    }
    return currencies

FILE_NAME = "currencies.txt"

def save_currencies_to_file(currencies):
    with open(FILE_NAME, "w") as file:
        for key, value in currencies.items():
            line = f"{key}|{value['name']}|{value['alias']}|{value['in_usd']}\n"
            file.write(line)
    print("Currencies saved to file.")

def read_currencies_from_file():
    currencies = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    currencies[int(parts[0])] = {
                        'name': parts[1],
                        'alias': parts[2],
                        'in_usd': float(parts[3])
                    }
    except FileNotFoundError:
        print("File not found. Returning an empty dictionary.")
    return currencies

def add_currency_to_file(currency_id, name, alias, in_usd):
    with open(FILE_NAME, "a") as file:
        file.write(f"{currency_id}|{name}|{alias}|{in_usd}\n")
    print(f"Currency '{name}' added to file.")

def delete_currency(currencies):
    display_currencies(currencies)
    try:
        currency_id = int(input("Masukkan ID mata uang yang ingin dihapus: "))
        if currency_id not in currencies:
            print("ID tidak ditemukan.")
            return
        del currencies[currency_id]
        save_currencies_to_file(currencies)
        print("Mata uang berhasil dihapus.")
    except ValueError:
        print("Input tidak valid. Silakan coba lagi.")

def display_currencies(currencies):
    print("\nID | Name | Alias | In USD")
    print("----------------------------")
    for key, value in currencies.items():
        print(f"{key} | {value['name']} | {value['alias']} | {value['in_usd']}")

# Update currency di file teks
def update_currency(currencies):
    display_currencies(currencies)
    try:
        currency_id = int(input("Masukkan ID mata uang yang ingin diupdate: "))
        if currency_id not in currencies:
            print("ID tidak ditemukan.")
            return
        name = input("Masukkan nama mata uang baru: ")
        alias = input("Masukkan alias baru: ")
        in_usd = float(input("Masukkan nilai baru dalam USD: "))
        currencies[currency_id] = {'name': name, 'alias': alias, 'in_usd': in_usd}
        save_currencies_to_file(currencies)
        print("Mata uang berhasil diupdate.")
    except ValueError:
        print("Input tidak valid. Silakan coba lagi.")

def operasi_mata_uang(amount, from_currency, to_currency, units):
    # kita ubah ke dolar amerika dulu
    to_usd = amount / units[from_currency]['in_usd']

    # lalu kita ubah ke target mata uang
    converted_amount = to_usd * units[to_currency]['in_usd']

    # balikin nilai akhirnya
    return converted_amount
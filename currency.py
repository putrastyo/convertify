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


def operasi_mata_uang(amount, from_currency, to_currency, units):
    # kita ubah ke dolar amerika dulu
    to_usd = amount / units[from_currency]['in_usd']

    # lalu kita ubah ke target mata uang
    converted_amount = to_usd * units[to_currency]['in_usd']

    # balikin nilai akhirnya
    return converted_amount
'''
Anggota Kelompok :
    Haidar Prayoga(202351048)
    Irsyal Firmansyah(202351050)
    Alan Lanang Ichsan(202351052)
'''

import json

# Read JSON file
with open("data.json", "r") as data:
    data = json.load(data)

def show():
    if len(data) == 0:
        print("Anda belum memmiliki barang masuk untuk saat ini")
    else:
        # Determine maximum length of each column
        name_col_len = max(len((item["name"])) for item in data) + 4
        color_col_len = max(len(item["color"]) for item in data) + 4
        size_col_len = max(len(item["size"]) for item in data) + 4
        stock_col_len = max(len(str(item["stock"])) for item in data) + 4
        price_col_len = max(len(str(item["price"])) for item in data) + 4
        code_col_len = max(len(str(item["code"])) for item in data) + 4

        print("List Semua Barang Dalam Gudang")
        print("--------------------------------------------------------")
        # Print header
        print(
            f'{"NAME".ljust(name_col_len)} {"COLOR".ljust(color_col_len)} {"SIZE".ljust(size_col_len)} {"STOCK".ljust(stock_col_len)} {"PRICE".ljust(price_col_len)} {"CODE".ljust(code_col_len)}'
        )
        # Print rows
        for item in data:
            print(
                f"{item['name'].ljust(name_col_len)} {item['color'].ljust(color_col_len)} {item['size'].ljust(size_col_len)} {str(item['stock']).ljust(stock_col_len)} {str(item['price']).ljust(price_col_len)} {str(item['code']).ljust(code_col_len)}"
            )
        print("--------------------------------------------------------")
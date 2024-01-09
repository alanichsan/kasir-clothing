'''
Anggota Kelompok :
    Haidar Prayoga(202351048)
    Irsyal Firmansyah(202351050)
    Alan Lanang Ichsan(202351052)
'''

import json
import random
import sys
from show_inventories import show

# Read JSON file
with open("data.json", "r") as data:
    data = json.load(data)


def create():
    while True:
        name = input("nama kaos: ")
        if name == "":
            print("nama tidak boleh kosong!")
            continue
        color = input("warna kaos: ")
        size = input("size kaos: ")
        stock = input("stok kaos: ")
        try:
            stock = int(stock)
        except ValueError:
            print("stok tidak boleh kosong!")
            continue
        price = input("harga kaos: ")
        try:
            price = int(price)
        except ValueError:
            print("harga tidak boleh kosong!")
            continue

        break

    # Generate 4 digit code
    generate_code = random.randint(0000, 9999)

    # Add new data
    data.append(
        {
            "name": name,
            "color": color,
            "size": size,
            "stock": stock,
            "code": generate_code,
            "price": price,
        }
    )

    # Write updated data
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

    print("===== Create successfully! =====")
    print("-------------------------------------")
    sys.stdout.write("\n")
    inventories()


def update():
    if len(data) == 0:
        print("Anda belum memmiliki barang masuk untuk saat ini")
        print("-------------------------------------")
        sys.stdout.write("\n")
        inventories()
    else:
        while True:
            code = input("code barang: ")
            try:
                code = int(code)
            except ValueError:
                print("Invalid Code")
                continue
            break

        temporary = {}

        # Update specific field
        for item in data:
            if item['code'] == code:
                temporary = item
            else:
                continue

        if len(temporary) != 0:
            for item in data:
                if item['code'] == code:
                    stock = int(input("stok barang: "))
                    item["stock"] = item["stock"] + stock
                    
                    with open("data.json", "w") as f:
                        json.dump(data, f, indent=4)

                    print("===== Update successfully! =====")
                    print("-------------------------------------")
                    sys.stdout.write("\n")
                    inventories()
        else:
            print("Invalid Code")
            sys.stdout.write("\n")
            update()


def menus():
    list_menu = ["1. Memasukan barang", "2. Merubah barang", "3. Keluar"]
    for menu in list_menu:
        print(menu)


def inventories():
    sys.stdout.write("\n")
    show()
    sys.stdout.write("\n")
    menus()
    select_menu = int(input("pilih menu (contoh: 1): "))

    match select_menu:
        case 1:
            create()
        case 2:
            update()
        case 3:
            exit()
        case _:
            print("menu tidak tersedia")

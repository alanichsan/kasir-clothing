import json
import sys
from show_inventories import show
from show_cart import showCart

# Read JSON file
with open("data.json", "r") as data:
    data = json.load(data)


def purchaseMenus():
    list_menu = ["1. Beli barang lagi?", "2. lihat keranjang", "3. Selesai"]
    for menu in list_menu:
        print(menu)


def purchase(cart):
    while True:
        code = input("Masukkan kode produk: ")
        if code == "" or int(code) <= 0:
            continue

        while True:
            quantity = input("Masukkan quantity: ")
            # Validasi quantity
            if not quantity:
                print("Quantity tidak boleh kosong!")
                continue

            if not quantity.isdigit():
                print("Quantity harus berupa angka!")
                continue

            break

        # Ubah ke integer
        quantity = int(quantity)

        # Validasi range quantity
        if quantity <= 0:
            print("Quantity harus lebih dari 0!")
            continue

        # Cari produk berdasarkan kode
        selected_products = [p for p in data if p["code"] == int(code)]

        if selected_products:
            product = selected_products[0]

            # Validasi stok
            if product["stock"] < quantity:
                print("Stok tidak mencukupi.")
                continue

            # Kurangi stok
            product["stock"] -= quantity

            # Tambahkan ke keranjang
            item = {"product": product, "qty": quantity}
            cart.append(item)

            print(f"{product['name']} berhasil ditambahkan ke keranjang.")
            sys.stdout.write("\n")
            purchaseMenus()
            while True:
                select_menu = int(input("pilih menu (contoh: 1): "))
                match select_menu:
                    case 1:
                        show()
                        purchase(cart)
                    case 2:
                        showCart(cart)
                        purchaseMenus()
                        continue
                    case 3:
                        break
                    case _:
                        print("menu tidak tersedia")
            break

        else:
            print("Produk tidak ditemukan.")

    # Hitung total
    total = 0
    for item in cart:
        product = item["product"]
        total += product["price"] * item["qty"]

    print(f"Total belanja: {total}")

    # Update file json dengan stok terbaru
    with open("data.json", "w") as f:
        json.dump(data, f)


def menus():
    list_menu = ["1. Beli barang", "2. Keluar"]
    for menu in list_menu:
        print(menu)


def shops():
    sys.stdout.write("\n")
    show()
    sys.stdout.write("\n")
    menus()
    select_menu = int(input("pilih menu (contoh: 1): "))

    match select_menu:
        case 1:
            purchase([])
        case 2:
            exit()
        case _:
            print("menu tidak tersedia")

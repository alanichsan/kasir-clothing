'''
Anggota Kelompok :
    Haidar Prayoga(202351048)
    Irsyal Firmansyah(202351050)
    Alan Lanang Ichsan(202351052)
'''

def showCart(products):
    if len(products) == 0:
        print("Anda belum memmiliki barang masuk untuk saat ini")
    else:
        
        print("Your products:")

        # Print header
        print("%-10s %-20s %s" % ("Qty", "Item", "Price"))  

        # Print each item  
        for item in products:
            name = item["product"]["name"]
            price = item["product"]["price"]
            qty = item["qty"]
            print("%-10d %-20s %d" % (qty, name, price))
        

        # Print totals  
        total = sum(item["qty"] * item["product"]["price"] for item in products)  
        print("-" * 50)
        print("%-10s %-20s %d" % ("", "Total", total))
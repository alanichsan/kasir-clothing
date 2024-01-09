'''
Anggota Kelompok :
    Haidar Prayoga(202351048)
    Irsyal Firmansyah(202351050)
    Alan Lanang Ichsan(202351052)
'''

import json
import getpass
import sys
from inventories import inventories
from shops import shops

with open('user.json', 'r') as user:
    users = json.load(user)

def login():
    username = input('masukan username: ')
    password = getpass.getpass('masukan password: ')
    for user in users:
        if user["username"] == username and user["password"] == password:
            sys.stdout.write("\n")
            print("===== Login successful! =====")
            if user["role"] == 'seller':
                inventories()
            elif user["role"] == 'buyer':
                shops()
            break

    else:
        print("===== Invalid username or password =====")
        login()
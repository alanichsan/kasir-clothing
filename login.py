import json
import getpass
from barang_masuk import barangMasuk

with open('user.json', 'r') as user:
    data = json.load(user)

def login():
    username = input('masukan username: ')
    password = getpass.getpass('masukan password: ')
    log_username = any(dictionary.get('username') == username for dictionary in data)
    log_pass = any(dictionary.get('password') == password for dictionary in data)
    if log_username and log_pass:
        print("===== Login successful! =====")
        barangMasuk()
    else:
        print("===== Invalid username or password =====")
        login()
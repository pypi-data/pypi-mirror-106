"""
pymd5search use case
"""

import secrets
import hashlib

def find():
    record = 0
    while True:
        my_string = secrets.token_hex(16)
        my_md5 = hashlib.md5(my_string.encode('utf-8')).hexdigest()
        compare = ""
        compteur = 0
        for x, y in zip(my_string, my_md5):
            if x == y:
                compare = compare + x
                compteur = compteur + 1
            else:
                compare = compare + "."    
        if compteur > record:
            print(my_string)
            print(my_md5)
            print(compare)
            record = compteur
            print("New record with " + str(record) + " commons characters")
            print("")
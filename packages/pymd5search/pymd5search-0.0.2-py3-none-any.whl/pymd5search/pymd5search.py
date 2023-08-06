"""
pymd5search use case
"""

import secrets
import hashlib
from pymd5search.args import compute_args

def find():

    isdebug = compute_args().debug
    numbercount = -1
    start = compute_args().start
    if start:
        my_md5 = start
    if compute_args().count:
        numbercount = compute_args().count
    number = 1
    record = 0
    while True:
        if number == numbercount + 1:
            print("end of script")
            break
        if start:
            my_string = my_md5
        else:    
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
        if isdebug:
            print("[debug] number test    : " + str(number))
            print("[debug] string to test : " + my_string)
            print("[debug] md5 to test    : " + my_md5)
            print("[debug] matching       : " + compare)            
        if compteur > record:
            print("")
            print("number test    : " + str(number))
            print("string to test : " + my_string)
            print("md5 to test    : " + my_md5)
            print("matching       : " + compare)   
            record = compteur
            print("New record with " + str(record) + " commons characters")
            print("")
        number = number +1    
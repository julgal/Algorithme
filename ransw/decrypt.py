#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

files = [] 

for file in os.listdir():
    if file == "voldemort.py" \
            or file == "thekey.key" \
            or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
        print(f"File: {file}")

with open("thekey.key", "rb") as key:
    secret_key = key.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
        print("Files decryted")

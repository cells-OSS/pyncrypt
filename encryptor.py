import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    fileName = input("Which file do you want to encrypt?: ")

    files.append(fileName)
    break
    
print(files)

confirmationMessage = input("Are you sure you want to encrypt this file(y/N)?: ")

if confirmationMessage == "Y" or "y":
    
    key = Fernet.generate_key()

    with open("decryption_key.txt", "wb") as decryption_key:
        decryption_key.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

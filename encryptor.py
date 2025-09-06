import os
from cryptography.fernet import Fernet

file_input = input("File(s) to encrypt: ")

files = [f.strip() for f in file_input.split(',') if f.strip()]

for file in files:
    if not os.path.isfile(file):
        print(f"File(s) not found: {file}")
        exit()

print(files)

confirmationMessage = input("The file(s) shown above will be encrypted, are you sure(y/N)?: ")

if confirmationMessage.lower() == "y":
    key = Fernet.generate_key()

    with open("decryption_key.txt", "wb") as decryption_key:
        decryption_key.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

    print("File(s) encrypted successfully!")
else:
    print("Encryption canceled.")

# pyncrypt
A simple file encryption script made with Python.

This script will encrypt the files that you choose, the testing so far shows that it works with text files.

# USE AT YOUR OWN RISK
 
I AM NOT RESPONSIBLE FOR ANY DATA LOSS, THERE IS A DECRYPTOR SCRIPT ON A DIFFERENT REPOSITORY, WHICH CAN BE FOUND HERE:

https://github.com/cells-OSS/pydcrypt

This script has been inspired by NetworkChuck: https://www.youtube.com/watch?v=UtMMjXOlRQc

Credits to him, this script at core has the code from NetworkChuck. It's just a fun project I wanted to try, he on his video made a "ransomware", but i decided to take the code and change it from being a ransomware to being an encryption script.

# HOW TO USE?

First of all, make sure you have the file you want to encrypt in the same folder as the encryption script. Then run the script and type the name of the file(s) you want to encrypt(put a comma between the files if you want to encrypt more than one file at a time). It will ask you if you're sure you want to encrypt the file and if answered positively there will be a .txt file created with the name of "decryption_key.txt" and if you choose to encrypt more than one file at a time they will be sharing the same decryption key. Instructions on how to decrypt the files you have decrypted can be found on https://github.com/cells-OSS/pydcrypt
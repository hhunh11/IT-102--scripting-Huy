#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By 
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
from base64 import b64encode, b64decode
import os

key=os.urandom(16)
print("Generated AES Key:", key)

plaintext=input("Enter a plaintext message: ").encode()
padder=padding.PKCS7(128).padder()
padded_data=padder.update(plaintext)+padder.finalize()

iv=os.urandom(16)

cipher=Cipher(algorithms.AES(key),modes.CBC(iv),backend=default_backend())
encryptor=cipher.encryptor()
ciphertext=encryptor.update(padded_data)+encryptor.finalize()

print("Encrypted message: ",b64encode(ciphertext).decode())

decryptor=cipher.decryptor()
decryptext=decryptor.update(ciphertext)+decryptor.finalize()

unpadder=padding.PKCS7(128).unpadder()
unpadded_data=unpadder.update(decryptext)+unpadder.finalize()

print("Decrypted message: "+unpadded_data.decode())
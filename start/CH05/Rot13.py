#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By 
def rot13(text,shift):
    result=""
    for char in text:
        if char.isalpha():
            base= ord("a") if char.islower() else ord("A")
            result+=chr((ord(char)-base+shift) %26+base)
        else: result+=char
    return result

message=input("Enter a message: ")
shift=int(input("Enter the shift value: "))

encrypted=rot13(message,shift)
decrypted=rot13(encrypted,-shift)

print("Encrypted message: "+encrypted)

answer=input("Decrypt the message? (yes/no): ").lower()
if answer=="yes":
    print("Decrypted message: "+decrypted)

#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 
from passlib.hash import sha512_crypt

SHADOW_FILE=r"C:\Users\hhunh\OneDrive\Máy tính\IT-102--scripting-Huy\find_passwords\shadow.txt"
PASSWORD_FILE=r"C:\Users\hhunh\OneDrive\Máy tính\IT-102--scripting-Huy\find_passwords\top1000.txt"

successful_attempts=[]
try:
    with open(SHADOW_FILE,'r', encoding='utf-8') as sha, open(PASSWORD_FILE,'r',encoding='utf-8') as top10:
        shadows=sha.readlines()
        passwords=[pw.strip() for pw in top10.readlines()]
        
        for shadow in shadows:
            parts=shadow.split(":")
            if len(parts)<2 or "!" in parts[1] or "#" in parts[1]:
                continue
            username, hash_password=parts[0], parts[1].strip()
            for password in passwords:
                try:
                    if sha512_crypt.verify(password,hash_password):
                        successful_attempts.append((username,password))
                        print(f'cracked successfully => {username}: {password}')
                        break
                except ValueError:
                    continue
except FileNotFoundError as e:
    print("Error!")
if successful_attempts:
    print("--------------------")
    print("Passwords Cracked!")
    for username, password in successful_attempts:
        print(username+"'s password is: "+password)
else: print("no passwords cracked!")
#!/usr/bin/env python3
# Script that hashes a password
# By 
from passlib.hash import sha512_crypt
password=input("enter your password: ")
hashed_pw=sha512_crypt.hash(password)
print("hashed password: "+hashed_pw)
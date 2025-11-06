#!/usr/bin/env python3
# Script that hashes a password with provided salt
# By 
from passlib.hash import sha512_crypt
password=input("input your password: ")
salt=input("enter salt: ")
hashed_pw=sha512_crypt.using(salt=salt).hash(password)
print("hashed password: "+hashed_pw)
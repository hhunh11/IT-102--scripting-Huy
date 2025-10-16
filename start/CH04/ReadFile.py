#!/usr/bin/env python3
# Sample script that reads from a file
# By 
with open("hackme.txt","r") as f:
    print("Here is someone to hack - information")
    content=f.read()
    print(content)
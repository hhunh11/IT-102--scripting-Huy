#!/usr/bin/env python3
# Sample script that writes to a file
# By 
name=input("What is your name? ")
color=input("What is your favorite color? ")
petName=input("What is your first pet's name? ")
motherName=input("What is your mother's maiden name? ")
school=input("What elementary school did you attend? ")

with open("hackme.txt","w") as f:
    f.write("Name: "+name+"\n")
    f.write("Color: "+color+"\n")
    f.write("Pet name: "+petName+"\n")
    f.write("Mother name: "+motherName+"\n")
    f.write("Your school: "+school+"\n")

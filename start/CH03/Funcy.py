#!/usr/bin/env python3
# example workign with Functions
#By 
def send_message(times):
    for i in range(times):
        print("Yeah it is")
answer=input("Is today a good day? (y/n) ").lower()
if answer=="y":
    send_message(10)
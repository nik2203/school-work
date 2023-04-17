import socket
import threading
import os,time
from cryptography.fernet import Fernet

hn = socket.gethostname()
localIP = socket.gethostbyname(hn)
localPort = 20002
bufferSize = 1024

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
s.bind((localIP,localPort))


def send():
    while True:
        ms = input("\t\t\t\t >> ")
        if ms.lower() == "quit":  
            print("We're sad to see you go :(")
            time.sleep(1)
            print("Quitting now..")
            time.sleep(1)
            os._exit(1)
        sm = "{}: {}".format(nm,ms)
        sm = send1.encrypt(bytes(sm,'utf-8'))
        s.sendto(sm,(ip,int(port)))
        print("\n")
    
def rec():
    while True:
        msg = s.recvfrom(bufferSize)
        msg = str(rec1.decrypt(msg[0]),'utf-8')
        print(">>" + msg+"\n")

def send_key():
    sen_key = Fernet.generate_key()
    f1 = Fernet(sen_key)
    s.sendto(sen_key,(ip,int(port)))
    return f1

def rec_key():
    recv_key = list(s.recvfrom(bufferSize))[0]
    f2 = Fernet(recv_key)
    return f2

os.system("cls")
print("===================================================")
print("==\t\t\t\t\t\t ==")
print("==",end='')
print("\t\tWelcome to U-chat\t\t ",end='')
print("==")
print("==\t\t\t\t\t\t ==")
print("===================================================\n")
print("\t    Server is up and listening\t\n")
print("\n===================================================\n")
print(f"Your current IP is {localIP}:{localPort}")
print("\n===================================================\n")
nm = input("What name do you want to use?: ")
print("\n===================================================\n")
os.system("cls")
print("===================================================")
print("==\t\t\t\t\t\t ==\n")
print(f"  Welcome {nm}! We hope you enjoy using U-chat  ",end='')
print("\n")
print("==\t\t\t\t\t\t ==")
print("===================================================\n")
print("\nTo exit, type \"quit\"")
print("\n==================================================\n")
ip,port = input("To connect to someone, enter their IP address and port number: ").split()
print("Successfully connected\n")
os.system("cls")
print("========================================================")
print("==\t\t\t\t\t\t      ==")
print("==",end='')
print(f"  Say hi! You're now talking to {ip}:{port}  ",end='')
print("==")
print("==\t\t\t\t\t\t      ==")
print("========================================================\n")
global send1
send1 = send_key()
global rec1
rec1 = rec_key()
x1 = threading.Thread( target = send )
x2 = threading.Thread( target = rec )
x1.start()
x2.start()
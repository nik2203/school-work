import socket
import threading
import os,time

hn = socket.gethostname()
localIP = socket.gethostbyname(hn)
localPort = 20002

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
s.bind((localIP,localPort))


os.system("cls")
print("===================================================")
print("==",end="")
print("\t    Server up and listening          ",end='')
print("==")
print("===================================================")
print("\t\tWelcome to U-chat\t\n")
print(f"Your current IP is {localIP}:{localPort}")
nm = input("What name do you want to use?: ")
print(f"Welcome {nm}! We hope you enjoy using U-chat")
print("\nTo exit, type \"quit\"")
print("To disconnect, type \"disconnect\"")
ip,port = input("To connect to someone, enter their IP address and port number: ").split()

def send():
    while True:
        ms = input("\t\t\t\t >> ")
        if ms == "quit":
            print("We're sad to see you go :(")
            time.sleep(2)
            print("Quitting now..")
            time.sleep(1)
            os._exit(1)
        sm = "{}  : {}".format(nm,ms)
        s.sendto(sm.encode() , (ip,int(port)))

def rec():
    while True:
        msg = s.recvfrom(1024)
        print(">> " +  msg[0].decode()  )
        print(">> ")
x1 = threading.Thread( target = send )
x2 = threading.Thread( target = rec )

x1.start()
x2.start()
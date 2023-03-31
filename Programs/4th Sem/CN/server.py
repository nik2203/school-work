import socket
from os import system
from cryptography.fernet import Fernet

hn = socket.gethostname()
localIP = socket.gethostbyname(hn)
localPort = 20001
bufferSize = 1024

while(True):
    try:
        ex = 'n'
        UDPServerSocket = socket.socket(family = socket.AF_INET , type = socket.SOCK_DGRAM)
        UDPServerSocket.bind((localIP,localPort))
        system("cls")
        print("===================================================")
        print("==",end="")
        print("\t    UDP server up and listening          ",end='')
        print("==")
        print("===================================================")
        print("Note: You can only send one message at a time. Wait until the client message is received to send.\n")
        print(f"Current IP is: {localIP}")
        bytesAddressPair = list(UDPServerSocket.recvfrom(bufferSize))
        key = bytesAddressPair[0]
        f = Fernet(key)
        while(True):
            bytesAddressPair = list(UDPServerSocket.recvfrom(bufferSize))
            msgFromClient = f.decrypt(bytesAddressPair[0])
            msgFromClient = str(msgFromClient,'utf-8')
            address = bytesAddressPair[1]
            if(msgFromClient == "disconnect"):
                print("User disconnected\n")
                break
            print("Peer:",msgFromClient)
            msgFromServer = input("Me: ")
            msgFromServer = f.encrypt(bytes(msgFromServer,'utf-8'))
            UDPServerSocket.sendto(msgFromServer,address)
        ex = input("Do you want to exit (Y/N)\n")
        break
    except:
        print("\nSorry! We encountered an error! Please try again\n")
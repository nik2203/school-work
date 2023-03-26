import socket
from cryptography.fernet import Fernet

localIP = '127.0.0.1'
localPort = 20001
bufferSize = 1024

while(True):
    try:
        ex = 'n'
        UDPServerSocket = socket.socket(family = socket.AF_INET , type = socket.SOCK_DGRAM)
        UDPServerSocket.bind((localIP,localPort))
        print("UDP server up and listening")
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



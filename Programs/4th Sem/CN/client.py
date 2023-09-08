import socket
from os import system
from cryptography.fernet import Fernet
while(True):
    try:
        ex = 'n'
        serverAddressPort = (input("Enter the IP and port of the user to communicate with\n").split(','))
        serverAddressPort[1] = int(serverAddressPort[1])
        serverAddressPort = tuple(serverAddressPort)
        bufferSize = 1024
        disconnect = False
        UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
        key = Fernet.generate_key()
        f = Fernet(key)
        while(True):
            system("cls")
            print("===================================================")
            print("==",end="")
            print(f"    Successfully connected to {serverAddressPort[0]}\t ",end='')
            print("==")
            print("===================================================")
            print("Note: You can only send one message at a time.\n")
            UDPClientSocket.sendto(key,serverAddressPort)
            while(not disconnect):
                msgFromClient = input("Me: ")
                if (msgFromClient.lower() == "disconnect"):
                    msgFromClient = f.encrypt(bytes(msgFromClient,'utf-8'))
                    UDPClientSocket.sendto(msgFromClient,serverAddressPort)
                    break
                msgFromClient = f.encrypt(bytes(msgFromClient,'utf-8'))
                UDPClientSocket.sendto(msgFromClient,serverAddressPort)
                msgFromServer = list(UDPClientSocket.recvfrom(bufferSize))
                msg = f.decrypt(msgFromServer[0])
                msg = str(msg,'utf-8')
                print("Peer:",msg)
            print("Successfully disconnected from user\n")
            ex = input("Do you want to exit (Y/N)\n")
            break
        if(ex.lower() == 'y'):
            break
    except:
        print("\nSorry! We encountered an error! Please try again\n")
print("Successfully exited. Thank you for using our services.")
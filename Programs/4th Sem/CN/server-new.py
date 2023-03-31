import socket
from os import system
from cryptography.fernet import Fernet
from queue import Queue
from threading import Thread

hn = socket.gethostname()
localIP = socket.gethostbyname(hn)
localPort = 20001
bufferSize = 1024

# Create a queue to communicate between threads
q = Queue()

def receive_messages():
    global q
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))
    system("cls")
    print("===================================================")
    print("==", end="")
    print("\t    UDP server up and listening          ", end='')
    print("==")
    print("===================================================")
    print("Note: You can only send one message at a time. Wait until the client message is received to send.\n")
    print(f"Current IP is: {localIP}")
    bytesAddressPair = list(UDPServerSocket.recvfrom(bufferSize))
    key = bytesAddressPair[0]
    global f
    f = Fernet(key)
    while True:
        bytesAddressPair = list(UDPServerSocket.recvfrom(bufferSize))
        msgFromClient = f.decrypt(bytesAddressPair[0])
        msgFromClient = str(msgFromClient, 'utf-8')
        global address
        address = bytesAddressPair[1]
        if msgFromClient.lower() == "disconnect":
            q.put("User disconnected\n")
            break
        q.put(msgFromClient)

def send_messages():
    global q
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, 0))
    while True:
        # Wait for a message to send
        msgFromServer = q.get()
        if msgFromServer.lower() == "disconnect":
            msgFromServer = f.encrypt(bytes(msgFromServer, 'utf-8'))
            UDPServerSocket.sendto(msgFromServer, address)
            break
        msgFromServer = f.encrypt(bytes(msgFromServer, 'utf-8'))
        UDPServerSocket.sendto(msgFromServer, address)
        
# Start the receive_messages thread
recv_thread = Thread(target=receive_messages)
recv_thread.start()

# Start the send_messages thread
send_thread = Thread(target=send_messages)
send_thread.start()

# Wait for the threads to finish
recv_thread.join()
send_thread.join()

print("Successfully exited. Thank you for using our services.")

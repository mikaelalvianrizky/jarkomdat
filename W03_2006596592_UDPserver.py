#!/usr/bin/env python3

from socket import *

BUFFER_SIZE = 2048
SERVER_PORT = 2108

def operation():
    with socket(AF_INET, SOCK_DGRAM) as serverSocket:
        serverSocket.bind(('', SERVER_PORT))
        while 1:
            numbers, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)

            results = 3.14 * int(numbers)**2 
            modifiedMessage = str(results).encode()

            print('Numbers from client', numbers)
            print('Answer from Server', modifiedMessage)

            serverSocket.sendto(modifiedMessage, clientAddress)





def main():
    print('The server is ready to receive')
    operation()
    
if __name__ == "__main__":
    main()
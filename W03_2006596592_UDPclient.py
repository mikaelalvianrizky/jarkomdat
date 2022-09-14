#!/usr/bin/env python3

from socket import *


BUFFER_SIZE = 2048
SERVER_IP = 'localhost'
SERVER_PORT = 2108

def main():
    with socket(AF_INET, SOCK_DGRAM) as clientSocket:
        print("~~ Welcome to Simple Calculation Circle Area Program ~~")
        numbers = input("Input the radius: ")

        clientSocket.sendto(numbers.encode(),(SERVER_IP, SERVER_PORT))

        modifiedMessage, serverAddress = clientSocket.recvfrom(BUFFER_SIZE)

        print("Answer from server: ",modifiedMessage.decode())

    
if __name__ == "__main__":
    main()

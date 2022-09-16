#!/usr/bin/env python
import socket

SERVER_IP = "35.208.169.105"
SERVER_PORT = 2003
BUFFER_SIZE = 1024

def main():
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((SERVER_IP, SERVER_PORT))
    
    print("~~ Welcome to Simple Calculation Circle Area Program ~~")
    numbers = input("Input the radius: ")
    numbers_bytes = numbers.encode("UTF-8")

    sc.send(numbers_bytes)
    
    modifiedMessage_bytes = sc.recv(BUFFER_SIZE)
    modifiedMessage = modifiedMessage_bytes.decode("UTF-8")

    print('Answer From Server: ', modifiedMessage)

    sc.close()

if __name__ == "__main__":
    main()
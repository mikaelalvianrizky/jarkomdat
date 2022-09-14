#!/usr/bin/env python

import socket
import time

SERVER_IP = ""
SERVER_PORT = 2003
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.bind((SERVER_IP, SERVER_PORT))
        sc.listen(0)

        print("Example Socket Server Program")

        while True:
            connection, address = sc.accept()
            print(f"Receive connection from {address}")

            numbers_bytes = connection.recv(BUFFER_SIZE)
            numbers = numbers_bytes.decode("UTF-8")

            results = 3.14 * int(numbers)**2 
            modifiedMessage = str(results).encode("UTF-8")

            print('Numbers from client', numbers)
            print('Answer from Server', modifiedMessage)

            connection.send(modifiedMessage)
            connection.close()

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
from socket import *

users = {}
BUFFER_SIZE = 2048
SERVER_PORT = 2108

def hash(text:str):
    res=0
    for ch in text:
        res = (res*281  ^ ord(ch)*997) & 0xFFFFFFFF
    return res

def login(name):
    userID = hash(name)
    users[userID] = name
    print(f"User ID Anda: {userID}")

def isValid(user_id):
    print(users)
    try:
        return int(user_id) in users
    except ValueError:
        return False

def operation():
    with socket(AF_INET, SOCK_DGRAM) as serverSocket:
        serverSocket.bind(('', SERVER_PORT))
        while 1:
            option, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
            option = option.decode('UTF-8')
            if(option=="1"):
                username, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
                username = username.decode('UTF-8')

                login(username)

            elif(option=="2"):
                user_id, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
                user_id = user_id.decode('UTF-8')

                if(isValid(user_id)):
                    radius, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
                    radius = radius.decode('UTF-8')

                    results = 3.14 * int(radius)**2 
                    modifiedMessage = str(results).encode()
                    serverSocket.sendto(modifiedMessage, clientAddress)

                    print('Radius from client', radius)
                    print('Answer from Server', modifiedMessage)
                
                else:
                    modifiedMessage = "ID tersebut belum terdaftar!".encode()
                    serverSocket.sendto(modifiedMessage, clientAddress)

                    print("ID tersebut belum terdaftar!")
            
            else:
                user_id, clientAddress = serverSocket.recvfrom(BUFFER_SIZE)
                user_id = int(user_id.decode('UTF-8'))
                users.pop(user_id)

def main():
    print('The server is ready to receive')
    operation()
    
if __name__ == "__main__":
    main()
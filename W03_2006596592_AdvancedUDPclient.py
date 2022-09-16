#!/usr/bin/env python3
from cmath import log
from socket import *
import string
from random import choice

users = {}
BUFFER_SIZE = 2048
SERVER_IP = '35.208.169.105'
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
    try:
        return int(user_id) in users
    except ValueError:
        return False

def main():
    with socket(AF_INET, SOCK_DGRAM) as clientSocket:
        while True:
            print("~~ Welcome to Mikael Program ~~")
            print("""
            1. Login
            2. Enter Calculation Circle Area
            3. Logout
            """)
            
            option = input("Select what you wanna do: ")
            clientSocket.sendto(option.encode(),(SERVER_IP, SERVER_PORT))
            if(option == "1"):
                username = input("Enter username: ")
                clientSocket.sendto(username.encode(),(SERVER_IP, SERVER_PORT))
                login(username)
            elif(option=="2"):
                user_id = input("Your ID: ")
                clientSocket.sendto(user_id.encode(),(SERVER_IP, SERVER_PORT))
                if(isValid(user_id)):
                    radius = input("Input the radius: ")
                    clientSocket.sendto(radius.encode(),(SERVER_IP, SERVER_PORT))
                    modifiedMessage, serverAddress = clientSocket.recvfrom(BUFFER_SIZE)
                    print("Answer from server: ", modifiedMessage.decode())
                else:
                    print("ID tersebut belum terdaftar!")
            else:
                user_id = input("Your ID: ")
                clientSocket.sendto(user_id.encode(),(SERVER_IP, SERVER_PORT))
                users.pop(int(user_id))

if __name__ == "__main__":
    main()

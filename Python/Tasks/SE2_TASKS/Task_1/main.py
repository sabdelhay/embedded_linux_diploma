#!/usr/bin/python3

import task1


def printMenu():
    print("Choose your favorite website: ")
    for key, site in task1.websites.items():
        print(f"{key}")

printMenu()

try:
    choice = input("Enter your favorite website: ").lower()
    if choice in task1.websites:
        task1.open_link(task1.websites[choice])
    else:
        print("Website in not found!")
except:
        print("Enter the right name!")
    
    

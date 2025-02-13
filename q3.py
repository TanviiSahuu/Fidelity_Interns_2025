#Create a class to find text files from given folder.

import os

folder = input("Enter the name of the folder: ")

def textfiles(folder):
    return [i for i in os.listdir(folder) if i.endswith(".txt")]

f = textfiles(folder)

print("Text Files:", f)


from DatabaseClass import*
from exifclasses import*
from imageprocessclasses import*
from User import*
import os
import sys


userInput = input("Welcome to a Database Manager for ImageLIB, type 'quit' to quit, or refer to commands sheet to learn database manipulation commands. ")

while userInput!="quit":
    if userInput.lower() == "add data":
        dataEntry()
        userInput = input()
    elif userInput.lower() == "remove data":
        tablename = input("Enter table name")
        filename = input("Enter file name")
        removeData(tablename,filename)
        userInput = input()
    elif userInput.lower() == "show data":
        tablename = input("Enter table name")
        columnname = input("Enter column name")
        displayData(tablename,columnname)
        userInput = input()

db.databaseconn3.close()
sys.exit()


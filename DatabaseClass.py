
import mysql.connector
from imageprocessclasses import*
import os
import getpass
import sys
print(os.getcwd())
from mysql.connector import errorcode
class Database(object):
    def __init__(self):
        self.username = input("Enter username ")
        self.password = getpass.getpass(prompt = "Enter password ")
        self.host = input("Enter host ")
        self.database = input("Enter database ") 
        self.databaseconn = self.connectTo(self.username,self.password,self.host)
        self.cursor = self.makeCursor(self.databaseconn)
    def connectTo (self, username,password,host):
        try:
            db = mysql.connector.connect(
                 user = username,
                 password = password,
                 host = host)
        except mysql.connector.Error as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Wrong login credentials")
                sys.exit()
            elif e.errno != errorcode.ER_BAD_DB_ERROR:
                print("error")
                sys.exit()
            else:
               pass
        else:
            return db

    def makeCursor(self,connection,):
        cursor = connection.cursor()
        return cursor
    def databaseConnect(self,cursor,connection,database):
        cursor.execute("CREATE DATABASE IF NOT EXISTS "+database)
        connection.database = database
    def makeTables(self,cursor):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Annotation_Manager(
                                        Image_File_Name char(75) NOT NULL,
                                        Annotation_Name char(15) NOT NULL,
                                        Annotation_ID char(75) NOT NULL,
                                        X_min float(10,2),
                                        Y_min float(10,2),
                                        X_max float(10,2),
                                        Y_max float(10,2))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Image_Information(
                                                Image_File_Name char(75) NOT NULL,
                                                Annotation_ID char(150) NOT NULL,
                                                Image_blob BLOB,
                                                Date_and_Time char(200),
                                                Latitude char(75),
                                                Longitude char(75))""")



    def dataInsertXML(self,cursor,listName,fileName):
        newList = listName
        for i in range(len(newList)):
            newList[i].insert(0,fileName)
        for j in newList:
            sqlcommand = "INSERT INTO Annotation_Manager (Image_File_Name,Annotation_Name,Annotation_ID,X_min,Y_min,X_max,Y_max) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            val = j
            cursor.execute(sqlcommand,val)
    def dataInsertImg(self,cursor,listName,fileName):
        newList = listName
        newList.insert(0,fileName)
        sqlcommand = "INSERT INTO IMAGE_INFORMATION (Image_File_Name,Annotation_ID,Image_blob,Date_and_Time,Latitude,Longitude) VALUES (%s,%s,%s,%s,%s,%s)"
        val = newList
        cursor.execute(sqlcommand,val)
    def datasetDelete(self,cursor,tablename,fileName):
        sqlcomm = "DELETE FROM "+tablename+" WHERE Image_File_Name = "+fileName
        cursor.execute(sqlcomm)

from DatabaseClass import*
from exifclasses import*
from imageprocessclasses import*
import os

db = Database()
db.databaseConnect(db.cursor,db.databaseconn,db.database)

#userInput = input("Welcome to a Database Manager for ImageLIB, type 'quit' to quit, or refer to commands sheet to learn database manipulation commands. ")



   
def dataEntry():
    
    inputFile = input("Enter text file name for file that lists ALL images and paired annotation files (each file on one line)")
    print("Make sure the text file with the images and annotations lists them on respective lines, with each image file \n being followed by its respective annotations file")
    with open(inputFile, 'r') as file:
        fileList = file.readlines()

    fileListFinal = []

    for x in fileList:
        fileListFinal.append(x.rstrip("\n"))

    for i in range(len(fileListFinal)):
        if ".xml" in fileListFinal[i]:
            newdataset = AnnotationID(fileListFinal[i])
            db.dataInsertXML(db.cursor,newdataset.finalList,fileListFinal[i])
        else:
            newdataset = exifList(fileListFinal[i])
            try:
                db.dataInsertImg(db.cursor,newdataset.finalList,fileListFinal[i])
            except AttributeError as e:
                i+=1


def displayData(tablename, columnname):
    db.cursor.execute("SELECT "+columnname+" FROM "+tablename)
    result = db.cursor.fetchall()
    for x in result:
        print(x)
def removeData(tablename,filename):
    db.datasetDelete(db.cursor,tablename,filename)






            
            

import xml.etree.ElementTree as ET

class xmlParse(object):
    def __init__(self,file):
        self.parsedata = ET.parse(""+file).getroot()

class xmlAnnotation(xmlParse):
    def __init__(self,file):#file must be string of file name
        super().__init__(file)
        self.annotationList = self.parseFile()
        self.names = self.parseName()
    def parseFile(self):
        annotList =[]
        for i in self.parsedata.findall('object'):
            name = i.find("name").text
            elementbnd = i.find("bndbox")
            xmin = float(elementbnd.find("xmin").text)
            ymin = float(elementbnd.find("ymin").text)
            xmax = float(elementbnd.find("xmax").text)
            ymax = float(elementbnd.find("ymax").text)
            data = (name,xmin,ymin,xmax,ymax)
            annotList.append(data)
        return annotList
    def parseName(self):
        nameList =[]
        for i in self.parsedata.findall('object'):
            nameList.append(i.find("name").text)            
        return nameList

class BasicAnnotation(xmlAnnotation):
    def __init__(self,file):
        super().__init__(file)


import random
class AnnotationID(BasicAnnotation):
    def rng(self):
        IdInit = ""
        for z in range(9):
            IdInit+= str(random.randrange(0,10))
            
        return IdInit

    def idCreator(self):
        nameID = []
        for j in self.names:
            nameID.append(j+self.rng())
        return nameID
    
    def __init__(self,file):
        super().__init__(file)
        self.customid = self.idCreator()
        self.finalList = self.combinedList(self.customid,self.annotationList)

    def printatt(self):
        print(self.customid)
        print(self.annotationList)
    def combinedList(self,idList,annotationsList):
        combinedList = [list(j) for j in annotationsList]
        for i in range(len(annotationsList)):
            combinedList[i].insert(1,idList[i])
        return combinedList
            
            


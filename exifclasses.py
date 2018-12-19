from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS
import os
print(os.listdir())
class exifList(object):
    def extractValue(self,img,keywords):
        photodatalist =[]
        imdata = img._getexif().items()
        for i in keywords:
            for k,v in imdata :
                try:
                    if(TAGS[k]==i or GPSTAGS[k]==i):
                        photodatalist.append(v)
                except KeyError as e:
                    pass
                else:
                    photodatalist.append("null")
        return photodatalist           
    def blobmaker (self,file):
        with open(file,'rb') as imgdata:
            blob = imgdata.read()
        return blob
    def __init__(self,file):      
        self.pieces = ["DateTimeOriginal","Latitude","Longitude"]
        self.im = Image.open(file)
        self.file = file
        self.blob = self.blobmaker(self.file)
        self.extractedData = self.extractValue(self.im,self.pieces)
        self.finalList = self.extractedData.insert(1,self.blob)
    



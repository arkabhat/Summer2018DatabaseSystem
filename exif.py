from PIL import Image
from PIL.ExifTags import TAGS
im = Image.open("TESTPICTURE.jpeg")

exifdata = im._getexif().items()
#print(exifdata)

exif = {
    TAGS[k]: v
    for k, v in im._getexif().items()
    if k in TAGS
}
print(exif)

def gettingExpectedItem(exif,keyword):
    for k,v in exif:
        if(TAGS[k]==keyword):
            print(v)

gettingExpectedItem(exifdata, "ExposureTime")


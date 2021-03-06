import os 
import pyqrcode
from PIL import Image
import png

class QR_Gen(object):
    def __init__(self,text):
        self.qr_image = self.qr_generator(text)

    @staticmethod
    def qr_generator(text):
        qr_code = pyqrcode.create(text)
        fileName = "Your QR Code"
        SavePath = os.path.join(os.path.expanduser('~'),'Desktop')

        name = f"{SavePath}{fileName}.png"
        qr_code.png(name,scale=10)
        image = Image.open(name)
        image = image.resize((400,400),Image.ANTIALIAS)
        image.show()

if __name__ == "__main__":
    QR_Gen(input("[QR] Enter text or link: "))

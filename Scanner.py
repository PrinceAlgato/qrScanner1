from email.mime import image
from tkinter import Scale
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = qrcode.make("annanya i really love you and i will always do until you love me 😁")
qr.save("my code", Scale= 8)

d = decode(image.open("my code"))
print(d)
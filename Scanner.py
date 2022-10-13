from email.mime import image
from tkinter import Scale
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = qrcode.make("hello😁")
qr.save("my code", Scale= 8)

d = decode(image.open("my code"))
print(d)
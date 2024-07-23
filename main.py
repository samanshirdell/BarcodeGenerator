import barcode
from barcode.writer import ImageWriter
from PIL import Image

numbers = input("Please enter the code to generate barcode: ")
barcode_format = barcode.get_barcode_class("upc")
barcode_ready = barcode_format(numbers, writer=ImageWriter())
barcode_ready.save("barcode_generate")
Image.open("barcode_generate.png")
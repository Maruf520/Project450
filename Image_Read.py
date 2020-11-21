import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Users\Maruf\AppData\Local\Tesseract-OCR\tesseract.exe'
 
from PIL import Image 
 
value=Image.open("C:/Users/Maruf/Pictures/test1.png") 
text = tess.image_to_string(value)
 
print(text)
# Import modules
from PIL import Image
import pytesseract

# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

# Create an image object of PIL library
image = Image.open('C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/Triada/test.jpg')

# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')

# Print the text
print(image_to_text)




'''
import os
import tempfile
import subprocess

def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r') as handle:
        contents = handle.read()

    os.remove(temp.name + '.txt')
    os.remove(temp.name)

    return contents

str = ocr('C:/Users/KEVINBONYTHEKKANATH-/Desktop/Projects/Triada/PTD_Groove.png')
print(str)
'''
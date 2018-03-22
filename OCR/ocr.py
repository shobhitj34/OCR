try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '<full_path_to_your_tesseract_executable>'

print(pytesseract.image_to_string(Image.open('test.png')))
print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))


import cv2

img = cv2.imread('/**path_to_image**/digits.png')
print(pytesseract.image_to_string(img))
print(pytesseract.image_to_string(Image.fromarray(img))
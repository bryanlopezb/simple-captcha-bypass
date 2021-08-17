# Import OpenCV for image processing and Pytesseract to extract text.
import cv2 
import pytesseract

#Read image, locally stored for now
img = cv2.imread('captcha.png')

#PoC
text = pytesseract.image_to_string(img)
print(text)
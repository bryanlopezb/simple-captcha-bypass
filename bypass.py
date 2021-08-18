# Import OpenCV for image processing and Pytesseract to extract text.
#Numpy for some denoise operations
import cv2 
import pytesseract
import numpy as np

#Read image, locally stored for now
img = cv2.imread('captcha4.jpeg')

#Some image processing
#Convert to gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
#Convert to binary
img_binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#Invert colors
inverse = cv2.bitwise_not(img_binary)

#Denoise
img_denoise = cv2.fastNlMeansDenoising(inverse, None, 10,7,21)

kernel = np.ones((2,2),np.uint8)
processed_img = cv2.erode(img_denoise, kernel, iterations = 1)
processed_img = cv2.dilate(processed_img, kernel, iterations = 1)
final = cv2.medianBlur(processed_img,1)

#PoC
#Show processed image
cv2.imshow('Example', final)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
text = pytesseract.image_to_string(final, lang='eng',
 config= '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz')
print( "El texto es:" + text)
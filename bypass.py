# Import OpenCV for image processing and Pytesseract to extract text.
import cv2 
import pytesseract

#Read image, locally stored for now
img = cv2.imread('captcha.png')

#Some image processing
#Invert colors
inverse = cv2.bitwise_not(img)
#Convert to gray
gray = cv2.cvtColor(inverse, cv2.COLOR_BGR2GRAY) 
#Convert to binary
img_binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)[1]
#Denoise
img_denoise = cv2.fastNlMeansDenoising(img_binary, None, 10,7,21)

#PoC
#Show processed image
cv2.imshow('Example', img_denoise)
cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
text = pytesseract.image_to_string(img_denoise)
print( "El texto es:" + text)
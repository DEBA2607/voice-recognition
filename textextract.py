import pytesseract
import cv2
import PIL.Image
myconfig = r"--psm 6 --oem 3"
text= pytesseract.image_to_string(PIL.Image.open(r"C:\Users\User\Pictures\Screenshots\Leap.png"),config=myconfig)
print(text)
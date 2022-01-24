import cv2 
#Reading QR Code
image = cv2.imread("filename.png")
detector = cv2.QRCodeDetector()
data = detector.detectAndDecode(image)
print(data[0])

import numpy as np
import cv2

def detectedPlate(image,X,Y,W,H):
    rect_image = image[Y : Y+H, X : X+W]
    return rect_image

cv2.namedWindow("output", cv2.WINDOW_NORMAL)       
im = cv2.imread("car1.jpg")

image = cv2.resize(im, (960, 540))

edges = cv2.Canny(image,100,200)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

height, width = edges.shape
imageContours = np.zeros((height, width, 3), dtype=np.uint8)

cnts = []

# Dimensions of the plate to be detected
X = 0
Y = 0
W = 0
H = 0

# Filtered contours
for c in contours:
    (x,y,w,h) = cv2.boundingRect(c)
    if 3 > w/h > 2 and w*h > 6700:
        cnts.append(c)
        X = x
        Y = y
        W = w
        H = h

#cv2.rectangle(image, (X,Y), (X+W,Y+H), (0,255,0),2)
rect_image = detectedPlate(image,X,Y,W,H)        
cv2.imshow('',rect_image)
cv2.waitKey(0) 

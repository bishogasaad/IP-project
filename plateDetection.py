import numpy as np
import cv2
from imutils import resize
def detectedPlate(image,X,Y,W,H):
    ratio = image.shape[1]/720
    rect_image = image[int(Y*ratio): int((Y+H)*ratio), int(X*ratio): int((X+W)*ratio)]
    return rect_image

def detectplate(im):

    image = resize(im, 720)
    image = cv2.bilateralFilter(image,10,300,300)
    edges = cv2.Canny(image, 100, 300)

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

        if 2.6 > w/h > 2 and w*h>4000:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cnts.append(c)
            X = x
            Y = y
            W = w
            H = h
    #cv2.rectangle(image, (X,Y), (X+W,Y+H), (0,255,0),2)
    rect_image = detectedPlate(im,X,Y,W,H)
    return rect_image

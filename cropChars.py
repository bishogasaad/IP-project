import cv2
import numpy as np
from plateDetection import *
from imutils import resize

def cropChars(image):

	image = cv2.absdiff(cv2.bilateralFilter(image,100,300,300),image)
	_, image = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
	image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	_, image = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY)
	image = resize(image, 512)
	image = image[int(image.shape[0]/3):int(image.shape[0] - 20), 20:496]
	contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	for c in contours:
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
		X = x
		Y = y
		W = w
		H = h


	cv2.namedWindow('test', cv2.WINDOW_NORMAL)
	cv2.imshow('test', image)
	cv2.waitKey()
	cv2.destroyAllWindows()

image = detectplate(cv2.imread('car.JPG'))
cropChars(image)
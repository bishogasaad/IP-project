import cv2
import numpy as np
from plateDetection import *
from cropChars import *
from imutils import resize
import operator

def segmentCharacters(image):

	kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(2,10))
	dilation = cv2.dilate(image, kernel, iterations =6)
	contours, _ = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

	chars = []
	x_cords = []

	for c in contours:
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
		chars.append(image[y:y+h, x:x+w])
		x_cords.append(x)
		X = x
		Y = y
		W = w
		H = h

	#cv2.imshow('',chars[0])
	cv2.waitKey(0)	
	return chars, x_cords 

def sortingCharacters(chars, x_cords):
	dic = {}
	for i in range(0,len(chars)):
		#cv2.imshow(''+str(i),chars[i])
		dic[str(i)] = x_cords[i]
		#print(x_cords[i], int(i))
		#print(chars[i].shape)
	sorted_d = sorted(dic.items(), key=operator.itemgetter(1))
	return sorted_d
	#cv2.waitKey(0)

if __name__ == '__main__':
	image = detectplate(cv2.imread('car.JPG'))
	charactered_image = cropChars(image)
	chars, x_cords = segmentCharacters(charactered_image)
	dic = sortingCharacters(chars, x_cords)
	print(dic)
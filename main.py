import cv2
from plateDetection import detectplate
from cropChars import *
from segmentChars import *
def main():

	img = cv2.imread('car2.JPG')
	plate = detectplate(img)
	chars = cropChars(plate)
	cv2.imshow('chars', chars)
	chars, x_cords = segmentCharacters(chars)
	dic = sortingCharacters(chars,x_cords)
	for index in dic:
		cv2.imshow('char',chars[index[0]])
		cv2.waitKey()
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()

import cv2
import numpy as np
from imutils import resize

def cropChars(image):
	image = resize(image, 512)
	img = image.copy()
	mask = np.zeros(image.shape,np.uint8)
	image = cv2.absdiff(cv2.bilateralFilter(image,100,300,300),image)
	_, image = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)
	image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	_, image = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY)
	mask_NoPad = mask.copy()
	start = 20
	pad = 10
	image = image[int(image.shape[0]/3):int(image.shape[0] - 20), start:496]
	image = cv2.erode(image, np.ones([3, 3]))
	image = cv2.dilate(image, np.ones([3, 3]))
	image = cv2.dilate(image, np.ones([3, 3]))
	image = cv2.blur(image, (10, 10))
	contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	for c in contours:
		x, y, w, h = cv2.boundingRect(c)
		mask[y+int(img.shape[0]/3)-pad:y+h+int(img.shape[0]/3)+pad, x+start-pad:x+w+start+pad] = 1
		mask_NoPad[y+int(img.shape[0]/3):y+h+int(img.shape[0]/3), x+start:x+w+start] = 1

	img = cv2.multiply(mask, img, dtype=0)

	img = cv2.erode(img, np.ones([3, 3]))
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img = cv2.dilate(img, np.ones([3, 3]))
	_, img = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
	img = cv2.multiply(cv2.medianBlur(img, 9), img)

	mask_NoPad = mask_NoPad*255
	mask_NoPad = 255-cv2.cvtColor(mask_NoPad, cv2.COLOR_BGR2GRAY)
	img = cv2.add(img, mask_NoPad)
	return 255 - img

import cv2
from plateDetection import detectplate
from cropChars import *
from segmentChars import *
from ocr import ocr
import sys

def main():
	image_paths = ['car.JPG']
	if len(sys.argv) != 1:
		image_paths = sys.argv[1:]
	else:
		print('Warning: Missing image path. Will use default image ('+image_paths[0]+')')
		print('Usage main.py <image_path> [<image_path> [...]]')
	for i, image_path in enumerate(image_paths):
		img = cv2.imread(image_path)
		plate = detectplate(img)
		chars = cropChars(plate)
		cv2.imshow('chars'+str(i), chars)
		chars, x_cords = segmentCharacters(chars)
		dic = sortingCharacters(chars,x_cords)
		chars_text = []
		for index, x in dic:
			char_img = chars[index]
			char_img = cv2.bitwise_not(char_img)
			chars_text.append(ocr(char_img))
			# cv2.imshow('char',char_img)
			# cv2.waitKey(0)
			# cv2.imwrite('./output/'+str(x)+'.png', char_img)
		print(chars_text)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()

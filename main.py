import cv2
from plateDetection import detectplate
from cropChars import *
from segmentChars import *
from ocr import ocr
import sys
import json

def main():
	program_options = processArguments()
	if program_options['help']:
		printUsage()
		exit()
	if len(program_options['image_paths']) == 0:
		program_options['image_paths'].append('car.JPG')
		print('Warning: Missing image path. Will use default image ('+program_options['image_paths'][0]+')')
		printUsage()
	for i, image_path in enumerate(program_options['image_paths']):
		img = cv2.imread(image_path)
		plate = detectplate(img)
		chars = cropChars(plate)
		if not program_options['silent']:
			cv2.imshow('plate'+str(i), plate)
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
		if program_options['output'] == 'json':
			output = {
				'plates': [
					chars_text
				]
			}
			print(json.dumps(output))
		else:
			print(' '.join(chars_text))
	if not program_options['silent']:
		cv2.waitKey(0)
		cv2.destroyAllWindows()


def printUsage():
	print('''python3 main.py [<options>] <image_path> [<image_path> [...]]
python3 main.py --help

Options:
-s, --silent:   do not show any windows, print output only
--json:         output in json format

-h, --help:     show this help message''')
	

def processArguments():
	# reads command line arguments,
	# returns a dictionary
	program_options = {
		'help': False,
		'silent': False,
		'output': 'simple',
		'image_paths': []
	}
	cmd_args = sys.argv[1:]
	for arg in cmd_args:
		if arg == '-h' or arg == '--help':
			program_options['help'] = True
		elif arg == '-s' or arg == '--silent':
			program_options['silent'] = True
		elif arg == '--json':
			program_options['output'] = 'json'
		else:
			program_options['image_paths'].append(arg)
	return program_options


if __name__ == '__main__':
	main()

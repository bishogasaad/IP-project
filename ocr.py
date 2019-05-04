from PIL import Image
import pytesseract

'''
    some tesseract config options:

    --psm N
    Set Tesseract to only run a subset of layout analysis and assume a certain form of image. The options for N are:

    0 = Orientation and script detection (OSD) only.
    1 = Automatic page segmentation with OSD.
    2 = Automatic page segmentation, but no OSD, or OCR. (not implemented)
    3 = Fully automatic page segmentation, but no OSD. (Default)
    4 = Assume a single column of text of variable sizes.
    5 = Assume a single uniform block of vertically aligned text.
    6 = Assume a single uniform block of text.
    7 = Treat the image as a single text line.
    8 = Treat the image as a single word.
    9 = Treat the image as a single word in a circle.
    10 = Treat the image as a single character.
    11 = Sparse text. Find as much text as possible in no particular order.
    12 = Sparse text with OSD.
    13 = Raw line. Treat the image as a single text line,
        bypassing hacks that are Tesseract-specific.

    --oem N
    Specify OCR Engine mode. The options for N are:

    0 = Original Tesseract only.
    1 = Neural nets LSTM only.
    2 = Tesseract + LSTM.
    3 = Default, based on what is available.
'''

def ocr(image):
    langs = ['ara', 'ara-Amiri', 'ara-Amiri-layer', 'ara-Scheherazade']
    lang = langs[1]
    oem = 1
    psm = 13
    config = '--oem ' + str(oem) + ' --psm ' + str(psm)
    char = pytesseract.image_to_string(image, lang=lang, config=config)
    char = char.strip()
    # use our prior knowledge to fix possible errors
    # char cannot be empty, nor can be more than one character
    if len(char) == 0 or len(char) > 1:
        psm = 10
        config = '--oem ' + str(oem) + ' --psm ' + str(psm)
        char = pytesseract.image_to_string(image, lang=lang, config=config)
        char = char.strip()
    # convert arabic numerals to english
    char = arabicToEnglishNumeralsChar(char)
    return char

def arabicToEnglishNumeralsChar(numeral):
    # returns english equivalent of numeral if it's
    # an arabic numeral, if not, returns it unchanged
    ar = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']
    en = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(10):
        if numeral == ar[i]:
            return en[i]
    return numeral

def arabicToEnglishNumeralsList(chars):
    # returns new list of chars, where each
    # arabic numeral is converted to its english
    # equivalent
    new_chars = list(chars)
    for i in range(len(chars)):
        chars[i] = arabicToEnglishNumeralsChar(chars[i])
    return new_chars
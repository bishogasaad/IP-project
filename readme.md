# Image Processing project

## Usage

```
python3 main.py [<options>] <image_path> [<image_path> [...]]
python3 main.py --help

Options:
-s, --silent:   do not show any windows, print output only
--json:         output in json format

-h, --help:     show this help message
```

---

## Installation

Install python3

### Required python packages:
``` sh
pip install opencv-contrib-python   # 4.1.0.25
pip install imutils                 # 0.5.2
pip install Pillow                  # 3.1.2
pip install pytesseract             # 0.2.6
```

### Required debian packages:
``` sh
# Install tesseract version 4
# https://launchpad.net/~alex-p/+archive/ubuntu/tesseract-ocr

sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
sudo apt install tesseract-ocr      # 4.1.0~git3875-b2fc3eba-1ppa1~xenial1
```

### Custom trained data for tesseract

1. Go to https://github.com/Shreeshrii/tessdata_arabic
1. Download these files to your system's `tessdata` directory (in Ubunutu: `/usr/share/tesseract-ocr/4.00/tessdata`)
    - ara-Amiri.traineddata
    - ara-Amiri-layer.traineddata
    - ara-Scheherazade.traineddata

Note: This project uses [tesseract](https://github.com/tesseract-ocr/tesseract) for OCR, with custom trained data for arabic taken from [here](https://github.com/Shreeshrii/tessdata_arabic), because default trained data does not recognize the hindi numerals (see this [issue comment](https://github.com/tesseract-ocr/tesseract/issues/2263#issuecomment-466675793) for more details)
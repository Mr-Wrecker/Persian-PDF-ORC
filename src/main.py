import argparse
import pathlib
from libs.pdf2img import Convertor

parser = argparse.ArgumentParser(
    description='''
    This Program Get a PDF File and Convert Each Page to JPEG.
    Then By i2ocr.com Extract Text in Each Image.
    So You Can Extract Text From Persian PDF.
    ''',
    epilog="usage: main.py -e -p /path/to/pdf/file.pdf"
)
parser.add_argument('-p', '--pdf', type=pathlib.Path,
                    help="PDF File Path to Convert JPEG")  # required: bool
parser.add_argument('-q', '--quality', type=int,
                    help="Quality Of Images. Such 100 to 1200")
parser.add_argument('-e', '--ocr', action='store_true',
                    help="Set True/False For Extract Text From JPEG")

args = parser.parse_args()


if __name__ == '__main__':
    print('Convert Successfully Done.') if Convertor(
        args.pdf, args.quality) else ('Some Things Wrongs!!!')

    if args.ocr:
        print(args.ocr)

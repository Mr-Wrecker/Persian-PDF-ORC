import os
from ._CONST import Image_Directory
from .cleaner import Cleaner


def Convertor(file, quality):
    Cleaner(Image_Directory, True)

    try:
        os.system(f"pdftoppm -jpeg -r {quality} {file} {Image_Directory}/IMG")
        return True
    except:
        return False

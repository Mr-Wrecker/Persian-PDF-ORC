import os
from ._CONST import Images_Path
from .clean import Cleaner


def Convertor(file, quality):
    Cleaner(Images_Path, True)

    try:
        os.system(f"pdftoppm -jpeg -r {quality} {file} {Images_Path}/IMG")
        return True
    except:
        return False

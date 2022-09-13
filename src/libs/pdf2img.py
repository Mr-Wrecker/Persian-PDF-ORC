import os
import re


def Convertor(file, quality):
    print("Convert Start ...")

    # Leaf directory
    directory = "Images"
    path = os.path.join(os.getcwd(), directory)
    if os.path.exists(path):
        print("Directory Exist ...")
    else:
        # Create the directory
        os.makedirs(path)

    try:
        os.system(f"pdftoppm -jpeg -r {quality} {file} Images/IMG")
        return True
    except:
        return False

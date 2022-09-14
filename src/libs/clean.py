import os
import shutil


def Cleaner(path, remove):
    # Leaf directory
    if os.path.exists(path) and remove:
        shutil.rmtree(path)

    # Create the directory
    os.makedirs(path, exist_ok=True)

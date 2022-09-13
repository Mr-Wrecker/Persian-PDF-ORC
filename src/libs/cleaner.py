import os
import shutil


def Cleaner(directory, remove):
    print(f"Create {directory}/ ...")

    # Leaf directory
    path = os.path.join(os.getcwd(), directory)
    if os.path.exists(path) and remove:
        shutil.rmtree(path)

    # Create the directory
    os.makedirs(path)

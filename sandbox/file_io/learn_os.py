from os.path import abspath, dirname
import os

import subprocess
try:
    import timeago
except ModuleNotFoundError as e:
    subprocess.call("pip install timeago")

# For getting full path of selected file
full_file_path = abspath('data.txt')

# For getting full path of executable file
full_file_path = os.path.abspath(__file__)

# For getting directory of the file
full_path = dirname(full_file_path)

# For creating single directory
os.mkdir("apple")
# OR
try:
    os.mkdir("apple/ball")
except FileNotFoundError as e:
    print("You have not created apple directory yet")

# For creating multiple hierarchy of directory
os.makedirs("cat/dog/elephant")

# For renaming directory
os.rename("elppa", "apple")

# For deleting single directory
os.rmdir("apple/ball")

# For deleting directory recursively
import shutil
shutil.rmtree("cat")
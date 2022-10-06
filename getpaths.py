"""
- get_file_paths.py

- Written by Jaesung-Jun
- Github : https://github.com/Jaesung-Jun
"""
import os
from tqdm import tqdm

class colors:
    GREEN = '\033[92m' #GREEN
    YELLO = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


def getNumberOfFiles(dirname):
    num_of_dir = 0
    for _, _, _ in os.walk(dirname, followlinks=True):
        num_of_dir = num_of_dir + 1
    return num_of_dir

def searchFilesInDirectory(dirname):
    files = []
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        ext = os.path.splitext(full_filename)[-1]
        if ext=='.jpg':
            files.append(full_filename)
    return files

def searchAllFiles(dirname, ext):

    filenames = []
    i = 0
    print(colors.GREEN + "Searching All Files in Directory.... \t\t directory name : " + dirname + colors.RESET)
    for path, _, files in tqdm(os.walk(dirname, followlinks=True)):
        i = i+1
        for name in files:
            full_filename = os.path.join(path, name)
            get_ext = os.path.splitext(full_filename)[-1]
            if get_ext == ("." + ext):
                filenames.append(os.path.join(path, name))

    return filenames


def searchAllFilesByDir(dirname, ext):

        files_by_path = []
        i = 0
        temp_path = ""
        print(colors.GREEN + "Searching All Files in Directory.... \t\t directory name : " + dirname + colors.RESET)
        for path, _, files in tqdm(os.walk(dirname, followlinks=True)):
            i = i+1
            if temp_path != path:
                temp = []
            for file in files:
                full_filename = os.path.join(path, file)
                get_ext = os.path.splitext(full_filename)[-1]
                if get_ext == ("." + ext):
                    temp.append(os.path.join(path, file))
            temp_path = path
            if temp != []:
                files_by_path.append(temp)

        return files_by_path

def printFileStructure(dirname, depth = 0):
    if depth == 0:
        print(colors.RED + dirname + colors.RESET)
    filenames = os.listdir(dirname)
    for filename in filenames:
        if os.path.isdir(dirname + "/" + filename):
            print("│", end="")
            for i in range(depth):
                print("   │", end="")
            print("┣" + filename)
            printFileStructure(dirname + "/" + filename, depth+1)
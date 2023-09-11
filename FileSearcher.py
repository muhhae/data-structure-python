import os

def ListFile(path, space = 0, fullPath = False, printType = False):
    spaceStr = '\t' * space
    print(f"{spaceStr}", sep="", end="")
    print(">", sep="", end="")
    printed = path if fullPath else os.path.basename(path)
    filetype = ""
    if os.path.isdir(path):
        if printType: filetype = "folder:"
        print(f"{filetype}{printed}")
        listDir = os.listdir(path)
        for e in listDir:
            ListFile(os.path.join(path, e), space + 1, fullPath, printType)
    else:
        if printType: filetype = "file:"
        print(f"{filetype}{printed}")

ListFile("D:/CPP_Fun_Project", 0, False, True)
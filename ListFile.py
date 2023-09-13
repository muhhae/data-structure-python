import os

def ListFile(path, space = 0, fullPath = False, printType = False):
    if not os.path.exists(path):
        print("Path doesnt exist")
        return
    print("\t" * space,"=>", sep="", end="")
    printed = path if fullPath else os.path.basename(path)
    filetype = ""
    if os.path.isdir(path):
        if printType: filetype = "folder:"
        print(filetype, printed)
        for e in os.listdir(path):
            ListFile(os.path.join(path, e), space + 1, fullPath, printType)
    else:
        if printType: filetype = "file:"
        print(filetype, printed)

ListFile("D:/CPP_Fun_Project/tetris-clone-sfml", 0, False, False)
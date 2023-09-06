import os

def ListFile(path, space = 0):
    listDir = os.listdir(path)
    for e in listDir:
        dir = os.path.join(path, e)
        for i in range(space):
            print("\t", sep="", end="")
        if os.path.isdir(dir):
            print(f"folder:{e}")
            ListFile(dir, space + 1)
        else:
            print(f"file:{e}")
ListFile("D:/CPP_Fun_Project")
import os

def ListFile(path):
    p = os.listdir(path)
    for e in p:
        dir = os.path.join(path, e)
        if os.path.isdir(dir):
            print(f"folder : {dir}")
            ListFile(dir)
        else:
            print(f"file : {dir}")

ListFile("D:/CPP_Fun_Project")
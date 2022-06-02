from os import listdir
from os.path import isfile, join

def find(path, filename)
    for f in listdir(path):
        os isfile(join(path, f)):
            if filename in f:
                print(f)
            else:
                find(join(path,f), filename)

find(r"D:\PSU\2nd Sem 2nd year\Software Design\Lab Reports 1-4","LAB 4- POSTLAB 2.26.py")
import os
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

path = r"C:\Users\jsantana\Downloads"
dictionary = {}

def storeFiles(path):
    dirs = os.listdir(path)
    list_path=[]
    list_file=[]
    list_extension=[]

    for file in dirs:
        path_d = os.path.join(path,file)
        root, ext = os.path.splitext(path_d)

        list_file.append(file)
        list_path.append(root)
        list_extension.append(ext)

    tuple_path = tuple(list_path)
    tuple_extension = tuple(list_extension)
    tuple_file = tuple(list_file)

    dictionary={"Path":tuple_path,"File":tuple_file,"Extension":tuple_extension}
    print(dictionary)

def get_all_file(dir_path, get_current = False):
    from pathlib import Path
    list = []

    files = [f.name for f in Path(dir_path).rglob("*.*")]
    ext = [f.suffix for f in Path(dir_path).rglob("*.*")]
    r = [f.anchor for f in Path(dir_path).rglob("*.*")]

    for i in files:
        root = os.path.join(path,i)
        list.append(root)

    dictionary={"Files":files,"Path":list,"Ext":ext}

    return dictionary



print(get_all_file(path))






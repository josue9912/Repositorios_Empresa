import os

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


print(storeFiles(path))





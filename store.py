import os

class StoreFiles():

     def __init__(self, root):
         self.root = root

     def saveFiles(self):


         for root, directories, files in os.walk(self.root, topdown=False):
             list_files = []
             list_directories = []

             for file in files:
                 list_files.append(file)
             tuple_files = tuple(list_files)

             for directory in directories:
                 list_directories.append(directory)
             tuple_directories = tuple(list_directories)

             dictionary = {"Files":tuple_files,"Directories":tuple_directories}

             print(dictionary)



if __name__ == '__main__':

    obj = StoreFiles('/Users/josuesantanagalvan')
    obj.saveFiles()







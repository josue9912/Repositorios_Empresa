import os
class Person():
    def __init__(self, _path):
        self._path = _path
    def buidDict(self):
        _list = []

        for items in os.listdir(self._path):
            data = {}
            path = os.path.join(self._path, items)
            root, extension = os.path.splitext(path)
            data['file_name'] = items
            data['file_path'] = root
            data['extension'] = extension
            _list.append(data)
        return _list

    def parseDict(self,key):
        for item in self.buidDict():
            for item, element in item.items():
                if not element:continue
                if item == key:
                    print(element)

ruta = r"C:\Users\jsantana\Downloads"
obj = Person(ruta).buidDict()
obj1= Person(ruta).parseDict('file_path')
print(obj1)
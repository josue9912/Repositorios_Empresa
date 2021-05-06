import os
import yaml
import io

thisdis = r"C:\Users\jsantana\Downloads"
# _list = []
# for item in os.listdir(thisdis):
#     datas = {}
#     path = os.path.join(thisdis,item)
#     root, extension = os.path.splitext(path)
#     datas['file_name'] = item
#     datas['file_path'] = root
#     datas['extension'] = extension
#     _list.append(datas)
#
#
# with io.open('data.yaml', 'w', encoding='utf8') as outfile:
#     yaml.dump(_list, outfile, default_flow_style=False, allow_unicode=True)


#Otra forma

_list = []
for item in os.listdir(thisdis):
    datas = {}
    path = os.path.join(thisdis,item)
    root, extension = os.path.splitext(path)
    datas['file_name'] = item
    datas['file_path'] = root
    datas['extension'] = extension
    _list.append(datas)
with io.open('data.yaml', 'w') as file:
 data = yaml.dump(_list,file)
 print(data)


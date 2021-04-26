import os
import shutil


thisdir = '/Users/josuesantanagalvan/Desktop/Carpeta_Prueba/Carpeta1/Carpeta2'


'''for r, d, f in os.walk(thisdir):

        for direcotorios in d:
            if "VFX" in direcotorios:
                try:
                    r1 = os.path.join(r, 'main')
                    os.mkdir(r1)
                except:
                    print("Ya existen las carpetas main")'''

for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".py"):

            old_root = os.path.join(r, file)
            new_file = file.replace('jercicio', '1')
            new_root = os.path.join(r, new_file)

            os.rename(old_root, new_root)

            nueva = r.replace("VFX","main")
            print(nueva)


            #shutil.move(new_root,nueva)








'''
            try:
                pass
               # shutil.move(new_root,r2)
            except:
                print("WTF BRO")


for r, d, f in os.walk(thisdir):
    for direcotorios in d:
        if "VFX" in direcotorios:
            print(r)'''












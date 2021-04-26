import os
import shutil

thisdir = '/Users/josuesantanagalvan/Desktop/Carpeta_Prueba/Carpeta1/Carpeta2'

for r, d, f in os.walk(thisdir):

    for direcotorios in d:
            if "VFX" in direcotorios:
                try:
                    r1 = os.path.join(r, 'main')
                    os.mkdir(r1)
                except:
                    print("Ya existen las carpetas main")


    for file in f:
         if file.endswith(".py"):
            old_root = os.path.join(r, file)
            new_file = file.replace('cicio', 'ssissio')
            new_root = os.path.join(r, new_file)

            os.rename(old_root, new_root)

            try:
                  shutil.move(new_root, os.path.join(r, 'main'))
            except:
                print("WTF BRO")







import os
import shutil


thisdir = '/Users/josuesantanagalvan/Desktop/Carpeta_Prueba/Carpeta1/Carpeta2'

for r, d, f in os.walk(thisdir):

        for directorios in d:
            if "VFX" in directorios:
                try:
                    r1 = os.path.join(r, 'main')
                    os.mkdir(r1)
                except:
                    print("Ya existen las carpetas main")

for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith(".py"):

            old_root = os.path.join(r, file)
            new_file = file.replace('jercicio', '1')
            new_root = os.path.join(r, new_file)
            os.rename(old_root, new_root)

for r, d, f in os.walk(thisdir):

    for file in f:

        if file.endswith(".py"):
            ruta_py = os.path.join(r,file)
            print(ruta_py)

            ruta_main = r.replace("VFX","main")
            print(ruta_main)

            try:
                shutil.move(ruta_py,ruta_main)
            except:
                print("Error en la ruta")

















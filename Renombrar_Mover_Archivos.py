import os
# coding: utf-8
import shutil

thisdir = "/Users/josuesantanagalvan/Desktop/Carpeta/Carpeta1/Carpeta2"

for r, d, f in os.walk(thisdir): #CREO CARPETAS
        if 'CarpetaFinal' in r:
            try:

                r1 = os.path.join(r, 'main')
                os.mkdir(r1)
                r2 = os.path.join(r, 'main','V01')
                os.mkdir(r2)

            except FileExistsError:
                print("Ya existen las carpetas main y V01")
                break

        for file in f: #MODIFICO EL NOMBRE DE LOS ARCHIVOS

            if file.endswith(".py"):

                old_root = os.path.join(r, file)
                new_file = file.replace('jercicio', '1')
                new_root = os.path.join(r, new_file)

                os.rename(old_root, new_root)
                destination_root = os.path.join(r, "main", "V01")

            try:
                #MUEVO EL FICHERO A LA CARPETA NUEVA
                shutil.move(new_root, destination_root)
            except:
                print("Error")

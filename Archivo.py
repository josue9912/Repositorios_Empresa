import os
# coding: utf-8
import shutil

thisdir = "/Users/josuesantanagalvan/Desktop/Carpeta/Carpeta1/Carpeta2"

for r, d, f in os.walk(thisdir): #Creo las carpetas

        if 'CarpetaFinal' in r:

            try:
                r1 = os.path.join(r, 'main')
                os.mkdir(r1)
                r2 = os.path.join(r, 'main','V01')
                os.mkdir(r2)

            except FileExistsError:
                break
                print("Ya existen las carpetas main y V01")


for r, d, f in os.walk(thisdir): #MODIFICO EL NOMBRE DE LOS ARCHIVOS
    for file in f:

        if file.endswith(".py"):


            ruta_antigua = os.path.join(r,file)
            nuevo_fichero = file.replace('jercicio','1')

            ruta_nueva = os.path.join(r,nuevo_fichero)
            os.rename(ruta_antigua,ruta_nueva)

            r_destino = os.path.join(r,"main","V01")


            try:

                shutil.move(ruta_nueva,r_destino)
            except:
                print("Error ")

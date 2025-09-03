# from io import open

# archivo_externo= open("Archivo1.txt", "r+")

# lista=archivo_externo.readlines()

# lista[1]="Leckovich\n"

# archivo_externo.seek(0)

# archivo_externo.writelines(lista)

# archivo_externo.seek(0)

# print(archivo_externo.read())

# archivo_externo.close()

import os

import io

#os.makedirs("Practica Directorio2")

os.chdir("../")

# archivo_externo=open("Practica2.docx", "w")

# archivo_externo.write("Texto Ejemplo")

#os.rename("Practica2.txt", "Archivo a Eliminar.txt")

#os.remove("Practica2.docx")

os.rmdir("Practica Directorio2")

print(os.getcwd())

#print(os.listdir("./"))

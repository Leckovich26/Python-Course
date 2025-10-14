#haciendo un diccionario

capitales={"Francia":"Paris", "Costa Rica":"San Jose", "Italia":"Roma"}

#Agregar un valor al diccionario

capitales["Colombia"]="Bogota"

#cambiar un valor en un diccionario

capitales["Francia"]="Toulousse"

print(capitales)

#eliminar un valor

del capitales["Colombia"]

print(capitales)

#agregar diferentes datos a un diccionario

datos={"Espana":"Madrid", 23:"Jordan", "Mosqueteros":3}

print(datos)

#usar tupla como claves para un diccionario

capitales=["Espana", "Reino Unido", "Colombia", "Costa Rica"]

capitalesPaises={capitales[0]:"Madrid", capitales[1]:"Londres", capitales[2]:"Bogota", capitales[3]:"San Jose"}

print(capitalesPaises)

#acceder un elemento en concreto de un diccionario/ hay que saber la clave

print(capitalesPaises["Espana"])

#saber cuales son las claves de un diccionario

print(capitalesPaises.keys())

#imprimir solo los valores de un diccionario

print(capitalesPaises.values())

#longitud de un diccionario

print(len(capitalesPaises))

#diccionarios anidados (un diccionario dentro de otro diccionario)

datosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"C Bulls", "Anillos":[1991,1992,1993,1996,1997,1998] }

print(datosJordan)

#ver solo los anillos

print(datosJordan["Anillos"])

#diccionario dentro de un diccionario

datosJordan={23:"Jordan", "Nombre":"Michael", "Equipo":"C Bulls", "Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998] }}

print(datosJordan.keys())

print(datosJordan)
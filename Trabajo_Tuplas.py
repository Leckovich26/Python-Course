#pasar de tupla a lista

misDatos=("Lecko", 26, 11, 1989, "Lecko")

misDatos=list(misDatos)

print(misDatos)

#pasar de lista a tupla

misDatosl=["Lecko", 26, 11, 1989]

misDatosl=tuple(misDatosl)

print(misDatosl)

#saber si un dato se encuentra en una tupla

print(26 in misDatos)
print("Lecko" in misDatos)

#saber cuantas veces se encuentra un texto en una tupla

print(misDatos.count("Lecko"))

#saber cuantos elementos tiene una tupla

print(len(misDatos))

#desempaquetar una tupla y ponerla en variables

nombre, dia, mes, ano, nombre=misDatos

print(nombre)

#tambien se pueden crear sin parentesis usando las comas

tupla= 1, 2, 3, 4, 5
print(tupla)
#ejercicio 1

nombre="Leckovich Gurdian"

contador=0

for i in nombre:
    if i==" ":
        continue
    contador+=1

print(contador)

#ejercicio 2

class Ejemplo:

    pass

#ejercicio 2

nombre="Leckovich Gurdian"

contador=0

for i in nombre:
    pass

    contador+=1

print(contador)


#ejercicio 4

email=input("Introduce un correo electronico: ")

for i in email:
    if "@" in email:
        arroba=True
        break
else:
    arroba=False

print(arroba)
#Ejercicio 1

Numeros= [25,30,50,37,14]

for i in Numeros:
    print("Hola Alumnos")

#Ejercicio 2

Meses=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

for i in Meses:
    print(i)

#Ejercicio 3 Range

for i in range(1,5):
    print("Hola a todos")

print("Fin del programa")

#Ejercicio de bucle

lista1= []
lista2= []

for i in range(1,6):
    lista1.append(input("Ingresa un nombre a lista 1: "))

for i in range(1,6):
    lista2.append(input("Ingresa un nombre a lista 2: "))

def comparacion(lista1,lista2):
    for i in lista1:
        if i in lista2:
            print(f"{i} esta en ambas listas.")
        else:
            print(f"{i} no se repite en las listas.")

comparacion(lista1,lista2)

#ejercicio de bucle extra

def comparalistas(lista1,lista2):
    if (len(lista1) != len(lista2)):
        return False
    else: 
        for i in range(1, len(lista1)):
            if(lista1[i] != lista2[i]):
                return False
    return True

alumnosA=["Juan", "Pedro", "Ana"]
alumnosB=["Juan", "Pedro", "Ana"]

print(comparalistas(alumnosA,alumnosB))


nombres=[]

intentos = 0

while True:
    try: 
        NuevoNombre= input("Introduce un nombre: ")

        if NuevoNombre in nombres:
            raise ValueError ("Error. Este nombre ya se ha introducido")
    
        else:
            nombres.append(NuevoNombre)

        intentos+=1

        if intentos == 3:

            break
    
    except ValueError as e:
        print(e)

print("\nLista de nombres introducidos: ")

for i, nombre in enumerate(nombres, start=1):
    print(f"{i}: {nombre}")

#segunda forma de como se podria lograr lo mismo

nombrepersonas=[]

def agregar_a_lista(lista,nombreInt):
    try:
        if nombreInt in lista:
            raise ValueError
        else:
            lista.append(nombreInt)
    except ValueError:
        print("Error. Este nombre ya se ha introducido.", nombreInt)

introducido=1

while introducido<11:
    nombre=input("Introduce un nombre: ")
    agregar_a_lista(nombrepersonas, nombre)
    introducido+=1

print(nombrepersonas)
#ejemplo uno de bucles while

contador=0

while contador<10:
    print("Hola")
    contador=contador+1
print("Hemos salido del bucle")

#ejemplo 2

import random

aleatorio= random.randint(1,100)

numero = int(input("Digite un numero: "))

intentos = 1

while numero!=aleatorio:
    
    if(numero<aleatorio):
        
        print("El numero es menor al numero aleatorio.")

    if(numero>aleatorio):
        
        print("El numero digitado es mayor al numero aleatorio.")
    
    numero=int(input("Digite un numero: "))

    intentos = intentos+1

print("Correcto. Has consumido " + str(intentos) + " intentos.")

#ejemplo 3

import math 

print("Este programa evalua la raiz cuadrada de un valor numerico")

numero=int(input("Introduce un numero: "))

intentos = 1

while numero < 0:
   
    print("El numero introducido no es valido")
    numero=int(input("Introduce un numero: "))
    intentos= intentos + 1
    if intentos==5:
    
        break

if intentos==5:
    print("Lo siento. No puedo realizar el calculo.")
else:
    print(math.sqrt(numero))

#ejercicio mejorado

import random

aleatorio= random.randint(1,100)

print("Este programa consiste en adivinar el numero secreto (entre 1 y 100)")

numero=int(input("Introduce un numero: "))
           
intentos = 1

while numero!= aleatorio:

    diferencia= abs(numero - aleatorio)

    if numero<aleatorio:
        print("El numero secreto es mayor.")
    else: 
        print("El numero secreto es menor")

    if diferencia <= 5:
        print("Muy caliente, estas muy cerca!")
    elif diferencia <= 15:
        print("Caliente, te estas acercando!")
    elif diferencia <=30:
        print("Tibio, aun lejos!")
    else: 
        print("Estas muy lejos!")
    
    numero=int(input("Introduce un numero: "))
    intentos= intentos + 1

print(f"¡Correcto! El número era {aleatorio}. Haz consumido {intentos} intentos")

        





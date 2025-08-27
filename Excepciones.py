import sys

def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def dividir(num1,num2):

    try: 

        return num1/num2
    
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
        return "Operacion erronea"

intentos = 0

while True: 
    try:

        opt1=int(input("Introduce el primer numero: "))

        opt2=int(input("Introduce el primer numero: "))

        break

    except ValueError:

        intentos += 1 

        print("Los valores introducidos no son correctos.")

        if intentos == 3:
            sys.exit()
  
opt3=input("Que tipo de operacion quieres realizar? (sumar,restar,multiplicar,dividir): ")

if opt3=="suma":
    print(suma(opt1,opt2))

elif opt3=="resta":
    print(resta(opt1,opt2))

elif opt3=="multiplicar":
    print(multiplicar(opt1,opt2))

elif opt3=="dividir":
    print(dividir(opt1,opt2))

else:
    print("Operacion no completada.")

print("Operacion ejecutada. Continuacion de ejecucion del programa.")
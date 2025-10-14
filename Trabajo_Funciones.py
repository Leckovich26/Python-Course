#definir funciones

def imprimirMensajes():
    
    print("Esto es un curso de python")

print("Esto no forma parte de la funcion")

imprimirMensajes()      #llama a la funcion

def imprimirValor():

    return "Este es el valor de la funcion" 

print(imprimirValor())

#guardan el valor que devuelve una funcion en una variable

VariableValor=imprimirValor()

print(VariableValor)

#crear funcion que reciba parametro

def imprimeMensajePersonalizado(mensaje, valor1, valor2):

    return mensaje + str((valor1+valor2))

print(imprimeMensajePersonalizado("La suma es: ",5,7))

#ejemplo 2 de funciones con parametros

def add_numbers(a,b):
    return "El resultado es: " + str(a+b)

result= add_numbers(5,5)

print(result)

#tercer ejemplo de una funcion con parametros

def rectangle_area(width, height):
    return width * height

result= rectangle_area(10,5)

print(result)

#cuarto ejemplo de una funcion con parametros

def CursoPasado(nota1, nota2):

    return nota1 + nota2

notafinal=  CursoPasado(35, 40)

print(notafinal)



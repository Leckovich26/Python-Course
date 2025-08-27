#Condicional con Else

mensaje = "Cual es la nota: "
int(input(mensaje))
nota = mensaje

def evaluar_alumno(nota):
    if nota <=5:
        valoracion = "Suspendido"
    else:
        valoracion = "Aprobado"
    print(valoracion)
    return valoracion

#Condicional basico

def NotaAlumno(nota):
    calificacion = "aprobado"
    if nota<5:
        calificacion = "suspenso"
    return calificacion

print(NotaAlumno(10))

#Ejemplo 3 con condicional

def Clima(temperatura):
    medicion = "desconocido"
    if temperatura < 15:
        medicion = "muy frio"
    else:
        medicion = "muy caliente"
    return medicion

PeticionTemperatura = int(input("Que temperatura hay: "))
print("La temperatura actualmente esta "+ str((Clima(PeticionTemperatura))))

#Ejemplo 4 Condicionales

def puntuacion(califique):
    
    NotaObtenida = "Pesimo"

    if califique == 2:
        NotaObtenida = "Malo"
    elif califique == 3:
        NotaObtenida = "Regular"
    elif califique == 4:
        NotaObtenida = "Bueno"
    elif califique == 5:
        NotaObtenida = "Excelente"
    elif califique <1 or califique > 5:
        NotaObtenida = "Digite un numero del 1 al 5"
    
    return NotaObtenida
    
DemeNota = int(input("Danos una calificacion del 1 al 5: "))

print (puntuacion(DemeNota))

#Ejemplo numero 5 de condicionales

fruits = ["manzana", "plátano", "cereza"]

frutas = input("Nombre de la fruta: ")

if frutas in fruits:
    print("La lista contiene esa fruta.")
else:
    print("La lista no contiene esa fruta.")


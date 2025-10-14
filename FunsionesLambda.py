
def triangulo():
        
        base=10
        altura=5

        division = (base*altura)/2

        return(division)

triangulo()

print(triangulo())

def triangulo2(base, altura):
        
        return (base*altura)/2

calculo=triangulo2(10,5)

print(calculo)

area_triangulo= lambda base1,altura1: (base1*altura1)/2

print(area_triangulo(10,5))

comision= lambda comision: "!{}!@".format(comision)

comision1=3000

print(comision(comision1))

lista=[(44,57),(8,4),(9,9),(25,32),(45,97)]

def ordenando(t):

    return t[0]+t[1]

lista.sort(key=ordenando)
print(lista)
lista.sort(key=lambda t:t[0]+t[1])
print(lista)


personas = [
    {"nombre": "Ana", "edad": 30},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Pedro", "edad": 40}
]

def por_edad(persona):      # persona es cada diccionario
    return persona["edad"]  # clave = edad

personas.sort(key=por_edad)
print(personas)


musicos=["Leckovich Gurdian", "Kerlyn Gonzalez", "Lilliam Alfaro", "Andres Mora"]

musicos.sort(key= lambda m: m.split()[1])

print(musicos)

frases=["Los lunes son los mejores días para programar","Python es moderno", "Veremos Inteligencia Artificial más adelante", "Lambda simplifica el código"]

frases.sort(key= lambda f:len(f.split()), reverse=True) 

print(frases)



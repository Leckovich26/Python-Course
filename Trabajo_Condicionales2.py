
print("Obtencion de carnet de conducir")

edad = int(input("Introduce tu edad: " ))

vision = input("Tu vision esta bien: ")

if edad>18 and edad <90 and vision == "Si":
    print("Puedes obtener tu licencia")
else:
    print("Lo siento. No cumples con los requisitos.")

#Ejemplo con condicionales con Operadores In y Not

trabajadores = ["Ana", "Juan", "Lecko", "Manuel", "Sandra", "Pedro25"]

if "Pedro" in trabajadores:
    print("Si, Pedro esta en la lista")

else:
    print("No, Pedro no esta en la lista")

# Ejemplo 2 de condicionales

lenguajes_Trim = "Java, Python, PHP, C#, HTML, JavaScript"

if "PHP" in lenguajes_Trim:
    print("si esta")

else: 
    print("no esta")

# Ejemplo 3 de condicionales

lenguajes_Trim = "Java, Python, PHP, C#, HTML, JavaScript"

if "SQL" not in lenguajes_Trim:
    print("Falta SQL")

else:
    print("SQL esta en la lista")    
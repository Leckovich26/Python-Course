
# ejercicio de condicionales donde se pide calcular el porcentaje a pagar dependiendo del valor de una propiedad.

def renta():
    monto= float(input("Cual es el monto de tu renta? "))
    if monto < 12000:
       print("A la renta introducida le toca pagar una tasa impositiva de un 7%.")   
    elif monto >=12000 and monto < 18000:
      print("A la renta introducida le toca pagar una tasa impositiva de un 15%.")
    elif monto >=18000 and monto < 35000:
       print("A la renta introducida le toca pagar una tasa impositiva de un 21%.")
    elif monto >=35000 and monto < 70000:
       print("A la renta introducida le toca pagar una tasa impositiva de un 35%.")
    else: 
        print("A la renta introducida le toca pagar una tasa impositiva de un 45%.")   

renta()

#Otras formas

def renta():
    monto= float(input("Cual es el monto de tu renta? "))
    if monto < 12000:
        tasa= 7
    elif 12000 <= monto < 18000:
        tasa= 15
    elif 18000 <= monto < 35000:
        tasa= 21
    elif 35000 <= monto < 70000:
        tasa= 35
    else:
        tasa= 45
    
    print(f"A la renta introducida le corresponde pagar un {tasa}%.")

renta()
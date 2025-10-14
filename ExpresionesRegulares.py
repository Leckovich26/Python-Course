import re

cadena="Estoy trabajando con python en domingo y semana santa"

busqueda="domingo"

if re.search("domingo", busqueda) is not None:

    print("Se encontro el termino", busqueda)

else:
    print("No se encontro", busqueda)

def buchacas():
    print("A mi me gusta tomar")



if re.findall("tomar", buchacas):
        print()

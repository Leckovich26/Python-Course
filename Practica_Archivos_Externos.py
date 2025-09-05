from io import *

fichero = open("Prueba Directorio/clientes.txt", "r", encoding="UTF-8")

lineas = fichero.readlines()

fichero.close()

clientes = []

for linea in lineas:

    campos = linea.split(";")

    cliente = {
        "Código": campos[0],
        "Nombre": campos[1],
        "Dirección": campos[2],
        "Población": campos[3],
        "Teléfono": campos[4],
        "Responsable": campos[5]
    }

    clientes.append(cliente)

for c in clientes:

    print("Código Artículo={} Nombre={} Dirección={} Población={} Tfno={} Responsable={}"
          .format(c["Código"], c["Nombre"], c["Dirección"], c["Población"], c["Teléfono"], c["Responsable"]))


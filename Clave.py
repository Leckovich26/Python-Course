import sqlite3

conexion=sqlite3.connect("Bases de Datos/GestionBBDD1")

Cursor=conexion.cursor()

# Cursor.execute('''
#     CREATE TABLE PRODUCTO1 (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_ARTICULO VARCHAR(40),
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)       
#                )
  
#                ''')

misproductos=[ 
    ("Camiseta", 34, "Moda"),
    ("Pantalon", 34, "Moda"),
    ("Coche", 34, "Jugueteria"),
    ("Gorra", 34, "Deportes")

]

Cursor.executemany("INSERT INTO PRODUCTO1 VALUES(NULL,?,?,?)", misproductos)

Cursor.execute("INSERT INTO PRODUCTO1 VALUES(NULL,'Boxer', 20, 'Accesorios')")

conexion.commit()

Cursor.close()

conexion.close()
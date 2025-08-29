edad = input("Introduce tu edad, por favor: ")

while (edad.isdigit()==False):
    print("El valor introducido no es correcto.")

    edad=input("Introduce tu edad, por favor: ")

if (int(edad)<(18)):
    print("No puedes pasar")

else:
    print("Puedes pasar")

#ejemplo2

class Persona():

    def __init__(self,nombre,apellido,edad):
        
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def __str__(self):
        return "Datos de la persona: \n" +self.nombre + "\nApellido: " +self.apellido + "\nEdad: " + str(self.edad)

p1=Persona("Lecko","Gurdian", 18)

print(p1)

#ejercicio 3

class Persona():

    almacendatos=[]
    
    def __init__(self, *datos):

        for i in datos:
            self.almacendatos.append(i)
        
        self.getDatos(self.almacendatos)

    def __str__(self): #esta funcion es una forma diferente de trabajar con parametros infinitos
        return "Datos de la persona: \n" +self.almacendatos[0] + "\n" +self.almacendatos[4] + "\n" + str(self.almacendatos[2])
    
    def getDatos(self, info):

        for i in info:
            print(i)

p1=Persona("Lecko","Gurdian", 18, 3500, "Hans")

print(p1)

#ejercicio 4

class agenda():

    def __init__(self):
        
        self.miagenda={}

    def agregarPersonas(self, nombre, telefono):

        self.miagenda[nombre]=telefono
    
    def __len__(self):
        return len(self.miagenda)
    
contactos=agenda()

contactos.agregarPersonas("Leckovich", 71054452)
contactos.agregarPersonas("Lilliam", 88130900)
contactos.agregarPersonas("Kerlyn", 87506951)
contactos.agregarPersonas("Roger", 72325294)

print(len(contactos))


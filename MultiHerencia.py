class persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def getDatosPersonales(self):
        return "Nombre: " + self.nombre + " Apellido: " + self.apellido + " Edad: " + str(self.edad)

    def habla(self):
        return "Estoy hablando."

    def piensa(self):
        return "Estoy pensando."

    def camina(self):
        return "Estoy caminando."

    def come(self):
        return "Estoy comiendo." 

class Estudiante(persona):

    def __init__(self, nombre, apellido, edad, escuela):
        persona.__init__(self, nombre, apellido, edad)

        self.escuela=escuela

    def getDatosPersonales(self):
        return super().getDatosPersonales() + " Escuela: " + self.escuela
    
    def estudia(self):
        return "Estoy estudiando."
    
class Trabajador(Estudiante):
    
    def __init__(self, nombre, apellido, edad, escuela, empresa):
        Estudiante.__init__(self, nombre, apellido, edad, escuela)
        self.empresa=empresa

    def getDatosPersonales(self):
        return super().getDatosPersonales() + "Empresa: " + self.empresa
    
    def trabaja(self):
        return "Estoy trabajando."
    
class Director(Trabajador, Estudiante):

    def __init__(self, nombre, apellido, edad, escuela, empresa, bonus):
        Trabajador.__init__(self,nombre, apellido, edad, empresa)
        Estudiante.__init__(self,nombre, apellido, edad, escuela)

        self.bonus=bonus

    def getDatosPersonales(self):
        return super().getDatosPersonales() + "Bonus: " + str(self.bonus)
    
    def dirige(self):
        return "Estoy dirigiendo"
    
persona1=persona("Lecko", "Gurdian", 35)

estudiante1= Estudiante("Hans", "Gurdian", 7, "San Javier")

print(persona1.getDatosPersonales())
print(estudiante1.getDatosPersonales())
print("-------------------------------------------------------------")

trabajador1=Trabajador("Kerlyn", "Lopez", 55, "Bedoya ", "Trabajando")
print(trabajador1.getDatosPersonales())


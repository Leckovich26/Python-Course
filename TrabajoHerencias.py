
class persona():

    def __init__(self, nombre, apellido, edad):

        self.nombre= nombre
        self.apellido= apellido
        self.edad= edad

    def getDatosPersonales(self):

        return "Nombre: " + self.nombre + "\nApellido: " + self.apellido + "\nEdad: " + str(self.edad)

    def habla():
        return "Estoy hablando"       
    
    def camina():
        return "Estoy caminando"
    
    def piensa():
        return "Estoy pensando"
    
    def come():
        return "Estoy comiendo"
    
class estudiante(persona):

    def __init__(self, nombre, apellido, edad, escuela):
        super().__init__(nombre, apellido, edad)

        self.escuela=escuela

    def getDatosPersonales(self):
        return super().getDatosPersonales() + "\nEscuela: " + self.escuela

    def estudia(self):
        return "Estoy estudiando"
    
persona1=persona("Leckovich ", "Gurdian ", 35)

estudiante1=estudiante("Kerlyn " , "Gonzalez ", 28, "Ramon Bedoya")

print(persona1.getDatosPersonales() + "\n")
print(estudiante1.getDatosPersonales())

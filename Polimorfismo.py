class Persona():

    def hablar(self):
        return "Hablo como una persona."
    
class Trabajador(Persona):

    def hablar(self):
        return "Hablo como un trabajador."
    
class Director(Trabajador):

    def hablar(self):
        return "Hablo como un director."

def hazlesHablar(loquesea):

    for i in loquesea:
        print(i.hablar())


Lecko=Persona()
Kerlyn=Trabajador()
Hans=Director()

print(Lecko.hablar())
print(Kerlyn.hablar())
print(Hans.hablar())

print("------------------------------------------------------")

listaPersonas=[Kerlyn,Hans,Lecko]

hazlesHablar(listaPersonas)
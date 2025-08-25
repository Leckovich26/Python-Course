
# class car():
#     llantas= 4
#     chasislargo= 260
#     chasisancho= 130
#     arrancado= False

#     def arrancar(self):
#         self.arrancado=True

#     def estadocar(self):
#         if (self.arrancado):
#             return "El carro esta funcionando."
        
#         else: 
#             return "El coche esta parado"

# mazda=car()

# renault=car()

# print(f"Tu coche tiene {str(mazda.llantas)} llantas")

# mazda.arrancar()

# print(f"Tu coche esta arrancado: {str(mazda.arrancado)}")

# print(renault.estadocar())

# #ejemplo 2 sobre clases

# class persona():
#     nombre=""
#     apellido=""
#     edad=0
#     genero=""

#     def __init__(self,nombre,apellido,edad,genero):
#         self.nombre=nombre
#         self.apellido=apellido
#         self.edad=edad
#         self.genero=genero
        
        
#     def habla(self):
#         return f"La persona que se llama {self.nombre} esta hablando."
    
#     def camina(self):
#         return f"La persona que se llama {self.nombre} esta caminando."
    
#     def getdatos(self):
#         return f"Nombre: {self.nombre} Apellido: {self.apellido} " \
#             f"Edad: {str(self.edad)} Genero: {self.genero}"
    
# persona1=persona("Lecko", "Gurdian", 21, "Masculino")

# print(persona1.getdatos())

# #ejercicio 3 sobre clases

# class CuentaCorriente():

#     NumeroCuenta=2548615425847
#     TitularCuenta=""
#     SaldoCuenta=0

#     def InformacionCuenta(self):
#         return f"Numero de cuenta: {self.NumeroCuenta} \nTitular de la Cuenta: {self.TitularCuenta}\n" \
#         f"Saldo en la Cuenta {self.SaldoCuenta}"

#     def DepositoDinero(self):
#         TitularCuenta=input("Nombre del titular de la cuenta: ")
#         monto= float(input("Dijista el monto que te gustaria depositar: "))
#         self.SaldoCuenta += monto
#         self.TitularCuenta = TitularCuenta

# Cliente1= CuentaCorriente()
# Cliente1.DepositoDinero()

# print(Cliente1.InformacionCuenta())

#ejemplo 4 sobre clases

class CuentaCorri():

    def __init__(self, number, title, total):
        
        self.number= number
        self.title= title
        self.total= total

    def getdata(self):

        return f"El titular de la cuenta # {self.number} es {self.title} "\
        f"y tiene un saldo en cuenta de {str(self.total)}"
    
    def ingresar(self, cantidad):
        self.total= self.total+ cantidad

    def retirar(self, cantidad):
        if cantidad>self.total:
            print("Saldo insuficiente.")
        
        else:
            self.total -= cantidad

cc1=CuentaCorri("2152459856", "Juan", 35000)

cc1.ingresar(5000)

cc1.retirar(40000)

print(cc1.getdata())


class CuentaCorriente():

    def __init__(self, NumeroCue, Titular, Total):

        self.NumeroCue= NumeroCue
        self.Titular= Titular
        self.Total= Total
    
    def getDatos(self):
        # return f"El numero de la cuenta {self.NumeroCue} "\
        #     f"de nombre {self.Titular} tienen un saldo de {str(self.Total)}"

        return f"Cuenta: {self.NumeroCue} | Titular: {self.Titular} | Saldo: {self.Total}"
    
    def ingresar(self, cantidad):
    
        self.Total+= cantidad

    def retirar(self, cantidad):

        if self.Total < cantidad:
            print (f"Saldo insuficiente.")

        else:
            self.Total-=cantidad


c1=CuentaCorriente(551515151, "Lecko", 5000)

class NuevaCuenta(CuentaCorriente):

    def __init__(self, NumeroCue, Titular, Total, bonus):
        super().__init__(NumeroCue, Titular, Total)
        
        self.bonus=bonus

    def bono(self, bonus):
        
        self.Total += bonus

    def getDatos(self):
        return super().getDatos()
    
    def ingresar(self, cantidad):
        return super().ingresar(cantidad)
    
    def retirar(self, cantidad):
        return super().retirar(cantidad)

print("Bienvenido a su cuenta bancaria.")

def menu():
    
    print("\n--- MENÚ BANCO ---")
    print("1: Depositar")
    print("2: Retirar")
    print("3: Consultar saldo")
    print("4: Aplicar bono")
    print("5: Salir")

    opciones = int(input("Elija una opción: "))
    
    monto = 0
    retiro = 0
    bono=0
    
    if opciones ==1:
        monto = int(input("¿Cuál es el monto a depositar?: "))
        print("Su deposito ha sido realizado satisfactoriamente.")
    
    elif opciones==2:
        retiro= int(input("¿Cuál es el monto a retirar?: "))

    elif opciones==3:
        pass

    elif opciones == 4:
        bono = int(input("Ingrese el monto del bono a aplicar: "))

    else:
        print("Opcion Invalida")

    return opciones, monto, retiro, bono

c2=NuevaCuenta(c1.NumeroCue, c1.Titular, c1.Total, 0)

while True:

    opciones, monto, retiro, bono = menu()

    if opciones==1:
        c2.ingresar(monto)
    elif opciones==2:
        c2.retirar(retiro)
    elif opciones==3:
        print(c2.getDatos())
    elif opciones == 4:
        c2.bono(bono)
        print(f"Bono aplicado: {bono}")
    elif opciones == 5:
        print("Gracias por usar el banco. Hasta luego!") 
        break
    else:
        print("Opción inválida. Intente nuevamente.")

print(c2.getDatos())  


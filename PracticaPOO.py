class CuentaCorri():

    def __init__(self, number, title, total):
        
        self.number= number
        self.title= title
        self.total= total

    def getdata(self):

        return f"El titular de la cuenta # {self.number} es {self.title} "\
        f"y tiene un saldo en cuenta de {str(self.total)}"
    
    def ingresar(self, cantidad):
        self.total += cantidad

    def retirar(self, cantidad):
        if cantidad>self.total:
            print("Saldo insuficiente.")
        
        else:
            self.total -= cantidad

# cc1=CuentaCorri("2152459856", "Juan", 35000)

# cc1.ingresar(5000)

# cc1.retirar(40000)

# print(cc1.getdata())

class CuentaJoven(CuentaCorri):

    def __init__(self, number, title, total, bonus_promocion):
        
        super().__init__(number,title,total)

        self.bonus_promocion= bonus_promocion

    def getBonus(self):

        self.total += self.bonus_promocion

        return f"El importe del bonus es de {self.bonus_promocion}"
    
    def ingresar(self, cantidad):
        return super().ingresar(cantidad)
    
    def retirar(self, cantidad):
        return super().retirar(cantidad)
    
    def getdata(self):
        return super().getdata()

cc2=CuentaJoven("21524658848", "Leckovich", 20000, 18000)    

cc2.ingresar(2500)

print(cc2.getBonus())

print(cc2.getdata())



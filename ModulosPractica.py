
class registros:

    def __init__(self):

        self.Diccionario={}

    def Usuario(self):
        while True:

            user=input("Digite su usuario: ")
                
            if len(user)<5:
                    print("El usuario no puede tener menos de 5 caracteres.")
                    
            elif len(user)>15:
                    print("El usuario no puede tener mas de 15 caracteres.")
                    
            elif not user.isalnum():
                    print("El usuario solo puede contener letras y números.")
                    
            else: 
                print("Usuario valido.")
                return user
                
    def Contraseña(self):

        while True:   
                
            passw=input("Digite su contraseña: ")
                
            if " " in passw:
                    print("La contraseña no puede tener espacios en blanco.")
                        
            elif len(passw)<10:
                    print("La contraseña tiene que tener minimo 10 caracteres.")
                        
            elif passw.isalnum():
                    print("La contraseña debe contener un caracter que no sea ni letra ni numero.")
                        
            elif not any(c.isupper() for c in passw):
                    print("La contraseña no es segura.")
                        
            else:
                print("Contraseña guardada.")
                return passw

    def registrar_usuario(self):
            usuario = self.Usuario()
            contrasena = self.Contraseña()
            self.Diccionario[usuario] = contrasena
            print("Registro completado:", self.Diccionario)

sistema = registros() 
sistema.registrar_usuario()
sistema.Diccionario

#version pro

import re  # Para validaciones avanzadas de contraseñas

class SistemaRegistro:
    def __init__(self):
        # Diccionario que almacena usuarios y contraseñas
        self.usuarios = {}

    # -----------------------
    # Validaciones
    # -----------------------
    def validar_usuario(self, user):
        if len(user) < 5:
            return "El usuario no puede tener menos de 5 caracteres."
        if len(user) > 15:
            return "El usuario no puede tener más de 15 caracteres."
        if not user.isalnum():
            return "El usuario solo puede contener letras y números."
        if user in self.usuarios:
            return "El usuario ya existe."
        return None  # Todo bien

    def validar_contraseña(self, passw):
        if " " in passw:
            return "La contraseña no puede tener espacios en blanco."
        if len(passw) < 10:
            return "La contraseña debe tener mínimo 10 caracteres."
        if passw.isalnum():
            return "La contraseña debe contener al menos un caracter que no sea ni letra ni número."
        if not any(c.isupper() for c in passw):
            return "La contraseña debe contener al menos una letra mayúscula."
        if not any(c.islower() for c in passw):
            return "La contraseña debe contener al menos una letra minúscula."
        if not any(c.isdigit() for c in passw):
            return "La contraseña debe contener al menos un número."
        return None  # Todo bien

    # -----------------------
    # Métodos principales
    # -----------------------
    def pedir_usuario(self):
        while True:
            user = input("Digite su usuario: ")
            error = self.validar_usuario(user)
            if error:
                print(error)
            else:
                print("Usuario válido.")
                return user

    def pedir_contraseña(self):
        while True:
            passw = input("Digite su contraseña: ")
            error = self.validar_contraseña(passw)
            if error:
                print(error)
            else:
                print("Contraseña guardada.")
                return passw

    def registrar_usuario(self):
        usuario = self.pedir_usuario()
        contrasena = self.pedir_contraseña()
        self.usuarios[usuario] = contrasena
        print("Registro completado.")

    def mostrar_usuarios(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print("-", usuario)

# -----------------------
# Uso del sistema
# -----------------------
sistema = SistemaRegistro()

# Registrar varios usuarios
while True:
    sistema.registrar_usuario()
    otra = input("¿Desea registrar otro usuario? (s/n): ").lower()
    if otra != "s":
        break

# Mostrar todos los usuarios
sistema.mostrar_usuarios()

def divide():

    try:

        op1=float(input("Introduce el pimer numero: "))

        op2=float(input("Introduce el segundo numero: "))

        print("El resultado de la division es " + str(op1/op2))

    except ZeroDivisionError:
        print("No se puede dividir por cero.")

    except ValueError:
        print("No se ingreso dato numerico.")

    except:
        print("Ha ocurrido un error.")

    finally:
        print("Se ha intentado de ejecutar la funcion en su totalidad.")
              
divide()

print("Exito, continuamos con el programa!")
"""Programa que permite identificar en una discoteca si puede ingresar o no dependiendo de la edad"""
nombre = str(input("Ingrese el nombre: "))
edad = int(input("ingrese la edad: "))
if edad > 18:
    print("Bienvendio, puede ingresar a la discoteca")
elif edad < 18:
    print("Lo siento, debes ser mayor de edad para ingresar al establecimiento")
else:
    print("por favor debe mostrar su identificacion para comprobar que su edad sea 18 ")
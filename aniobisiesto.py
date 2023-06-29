"""Programa que detecta si un año ingresado por el usuario es bisiesto o no"""
anio = int(input("ingrese el año que desea saber si es o no bisiesto: "))

if anio % 100 != 0:
    if anio % 4 == 0 or anio % 400 == 0:
        print("es año bisiesto")
    else:
        print(" no es un año bisiesto")

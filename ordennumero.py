"""Programa que muestra en pantalla en orden de mayor a menor dos numeros ingresados por el usuario, ademas muestra los numeros ingresados de forma aleatoria"""

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
print("los numero ingresados son: ", num1, "y ", num2)
if num1 > num2:
    print("y el orden correcto es: ", num1, ", ", num2)
elif num1 < num2:
    print("y el orden de mayor a menor es: ", num2, ", ", num1)
else:
    print("y los numero son iguales")
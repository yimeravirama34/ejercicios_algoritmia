"""Programa que muestra en pantalla en orden de mayor a menor de tres numeros ingresados por el usuario, ademas muestra los numeros ingresados de forma aleatoria"""

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))
print("los numero ingresados son: ", num1, ", ", num2, "y ", num3)
if num1 > num2 and num1 > num3:
    if num2 > num3:
        print("y el orden correcto es: ", num1, ", ", num2, ", ", num3)
    else:
        print("y el orden de mayor a menor es: ", num1, ", ", num3,  ", ", num2)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print("y el orden de mayor a menor es: ", num2, ", ", num1,  ", ", num3)
    else:
        print("y el orden de mayor a menor es: ", num2, ", ", num3,  ", ", num1)
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print("y el orden de mayor a menor es: ", num3, ", ", num1,  ", ", num2)
    else:
        print("y el orden de mayor a menor es: ", num3, ", ", num2,  ", ", num1)
else:
    print("hay dos o mas numeros ingresados son iguales ")
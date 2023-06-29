""" Programa que muestra la tabla de multiplicar ingresando el numero de la tabla que quiere conocer"""
num = int(input("ingrese la tabla que quiere conocer: "))
if num >= 0 and num <= 10:
    num1 = 1
    while num1 <= 10:
        res = num * num1
        print(num, " * ", num1, " = ", res)
        num1 = num1 + 1
elif num > 10:
    print("ingrese un entero entre 1 y 10")
else :
    print("ingrese valores positivos entre 1 y 10")

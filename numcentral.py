# Algoritmo que permite buscar cual es el central entre tres numero ingresados por el usuario

num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))
if num1<num3 and num1>num2 or num1>num3 and num1<num2:
        print("el numero central es: ", num1)

if num2<num3 and num2>num1 or num2<num1 and num2>num3:
        print("el numero central es: ", num2)

if num3<num1 and num3>num2 or num3>num1 and num3<num2:
        print("el numero central es: ", num3)

if num1 == num2 and num1 == num3:
    print("los numero son iguales : ", num3)
"""else:
    print("los numeros ingresados son iguales")
if num1 == num2:
    if num1 == num3:
        print("los tres numero son iguales a: ", num1)"""
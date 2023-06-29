num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))
if num1>num2:
    if num1>num3:
        print("el numero mayor es: ", num1)

if num2>num1:
    if  num2>num3:
        print("el numero mayor es: ", num2)

if num3>num2:
    if num3>num1:
        print("el numero mayor es: ", num3) 
else:
    print("los numeros ingresados son iguales")
"""if num1 == num2:
    if num1 == num3:
        print("los tres numero son iguales a: ", num1)"""
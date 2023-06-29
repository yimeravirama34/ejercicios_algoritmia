"""En el siguiente codigo se piden dos numeros al usuario y se le muestra en pantalla
el resultado de una suma, resta, producto, division, exponencial y modulo"""
num1 = float(input("ingrese el primer numero  a operar: "))
num2 = float(input("ingrese el segundo numero a operar: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1/num2
exp = num1**num2
mod = num1%num2
print("la suma es: ", suma)
print("la resta es: ", resta)
print("el producto es: ", producto)
print("la division es: ", division)
print("el exponencial es: ", exp)
print("el modulo es: ", mod)
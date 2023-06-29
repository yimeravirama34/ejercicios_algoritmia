"""A continucacion se muestra el codigo para conocer el resultado
de la potencia cuando el usuario ingresa la base y el exponente"""
base = float(input("ingrese el numero que tomara como la base: "))
exp = float(input("ingrese el valor del exponente: "))
while base == 0 and exp == -1:
    print("no se puede dividir por 0...")
    base = float(input("ingrese el numero que tomara como la base: "))
    exp = float(input("ingrese el valor del exponente: "))
potencia = base ** exp
print("la potecia de " + str(base) + " elevado al exponente " + str(exp) + " es: " + str(potencia))
masa = float(input("ingresar peso corporal: "))
talla = float(input("ingrese su altura: "))

imc = masa/talla**2
print(imc)
if imc < 18.5:
    print("bajo de peso")
if imc >= 18.5:
    if imc <= 24.9:
        print("saludable")
if imc >= 25:
    if imc <= 29.9:
        print("sobrepeso")
if imc >= 30:
    if imc <= 34.9:
        print("obesidad 1")
if imc >= 35:
    if imc <= 39.9:
        print("obesidad 2")
else :#imc > 40:
    print("obesidad 3")

#Algoritmo que me permite saber si un numero ingresado por teclado es par o impar

while True:
    try:
        numero = int(input("Por favor ingrese un numero: "))
        break
    except ValueError:
        print("Oops!  el valor ingresado no es valido, intente nuevamente...")

if numero % 2 == 0:
    print("el numero ", numero, " es par. ")
else:
    print("el numero ", numero, " es impar.")
#Algoritmo que permite al usuario ingresar un caracter y el programa le dice cual fue el tipo de caracter que ingreso

texto=input("ingrese numero: ")
if texto.isnumeric():
    print("Ingreso un numero mayor o igual a 0")
elif texto.isalpha():
    print("ingreso una letra")

else:
    print("ingreso un numero real ")
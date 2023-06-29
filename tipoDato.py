"""Programa para saber si lo que se ingreso es un numero, letra o decimal."""
caracter = input("ingrese el caracter a evaluar: ")

tipoDato = type(caracter)
print(tipoDato)
"""if tipoDato == str:
    print("es letra ")
elif tipoDato == int:
    print("es numero ")
elif tipoDato == float:
    print("es flotante ")
else:
    print(tipoDato, " es un simbolo ")"""

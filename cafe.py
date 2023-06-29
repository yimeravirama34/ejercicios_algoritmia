"""Programa que muestra a Tatiana la mejor opcion entre campanario o terraplaza para ir a tomar un cafe con su amiga Paola """
transporte = 1600
campanario = 0
terraplaza = 0
cafetp = 4000
dinero = float(input("Hola Tatiana, cuanto es tu dinero para decir cual es tu mejor opcion "))
# para campanario
campanario = 2 * transporte + cafetp
terraplaza = cafetp * 2 
if campanario < terraplaza:
    print("la mejor opcion para tomar un cafe es campanario")
elif terraplaza < campanario:
    print("la mejor opcion para tomar un cafe es en Terra Plaza ")
else:
    print("en cualquier lugar es igual")
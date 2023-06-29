"""Programa que permite calcular la velocidad si nos dan la distancia y su respectiva formula """
distancia = float(input("Ingrese la distancia en metros: "))

# como distancia = velocidad * tiempo
# despejando: velocidad = distancia/tiempo
if distancia > 20 and distancia < 35:
    tiempo = float(input("ingrese el tiempo en minutos para conocer la respectiva velocidad: "))
    velocidad = distancia / tiempo
    print("la velocidad es: ", velocidad, "m/seg. ")
else:
    print("la velocidad no esta dentro del rango para pedir un tiempo y poder calcular la velocidad")
    

#Algoritmo que permite mirar el pico placa
placa = input("ingre placa de su vehiculo: ")

if len(placa) == 6:
    try:
        x = int(placa[5])
    except:
        try:
            x = int(placa[4])
        except:
            print("placa ingresada no valida")

    if x == 1 or x == 2:
        print("tiene pico y palaca el viernes ")

    elif x == 3 or x == 4:
        print("tiene pico y placa el lunes ")

    elif x == 5 or x == 6:
        print("tiene pico y placa el martes ")

    elif x == 7 or x == 8:
        print("tiene pico y placa el miercoles ")

    elif x == 9 or x == 0:
        print("tiene pico y placa el jueves ")

    else:
        print("no tiene pico y placa")
else:
    print("la placa ingresada no es valida")
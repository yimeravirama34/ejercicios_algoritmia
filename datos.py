#Progama que me permite ingresar e imprimir en pantalla el nombre, la edad, identificacion y si es mayor de edad
nombre = str(input("ingrese el nombre: "))
edad = int(input("ingrese su edad: "))
estatura = 0
esta_viva = True 
apellido = "perez"
identificacion = float(input("ingrese el numero de su identificacion: "))
print(nombre, "tiene", edad, "años ", identificacion, " ID \n")#  "mide: ", estatura, "su estado es: ", esta_viva)
if edad >= 18:
    print("es mayor de edad ")
else:
    print("es menor de edad ")

#print(nombre, "tiene " + str(edad), "años " + "mide: " + str(estatura), "su estado es: "+ str( esta_viva))
#print(nombre + " "  + apellido)
#print("su nombre es %s" %(nombre) )
#print("su nombre es {}" , format(apellido))
# comentarios por lineas

''' cometarios
mas largos
'''
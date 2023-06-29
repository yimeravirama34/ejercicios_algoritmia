"""Algoritmo que permite calcular la nomina semanal, el salario neto mensual de los empleados y el total de impuestos a pagar dependiendo de las horas que se hayan trabajado, los datos como: 
nombre del empleado, horas semanales y precio seran ingresadas por teclado"""

nombre = str(input("ingrese el nombre del empleado: "))
horas = int(input("ingrese numeo de horas de trabajo del empleado:")) #d de tipo entero porque se maneja nominal de españa 
tarifa = float(input("ingrese la tarifa por hora: "))
salario = 0
#hora_extra= 0
if horas >= 0 and horas <=35:
    salario = (horas * tarifa) * 4
elif horas > 35:
    hora_extra = horas - 35
    salario = (35 * tarifa + hora_extra * tarifa * 1.5) *4
else:
    print("el numero de horas ingresadas no correspondena al trabajo ")

if salario <= 2000:
    print("esta libre de impuesto, su salario total mensual es: ",salario )
elif salario > 2000 and salario <= 2220:
    impuesto = salario * 0.2
    salario = salario - impuesto
    print("Ud debe pagar de impuestos: ", impuesto, ", y su salario neto queda: ", salario)
elif salario > 2220:
    impuesto = salario * 0.3
    salario = salario - impuesto
    print("Ud debe pagar de impuestos: ", impuesto, ", y su salario neto queda: ", salario)
#else:
# print("los datos ingresados estan incorrectos")
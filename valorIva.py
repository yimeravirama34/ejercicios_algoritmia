"""En este programa se calcula el IVA de un producto y le muestra al usuario cuanto paga en iva y cuanto es su descuento"""
valor = float(input("ingrese el valor del producto: "))
descuento = float(input("ingrese el descuento del producto: "))
iva = valor * 19/100
desc = valor - descuento
print("el iva de 19 por ciento de " + str(valor) + "es: " + str (iva))
print("el descuento del valor de su producto es: " + str(desc))

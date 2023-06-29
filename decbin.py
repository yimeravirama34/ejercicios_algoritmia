num = int(input(" digite el numero. "))
cociente = num
binario = ""
while cociente > 0:
    if cociente % 2 == 0:
        binario = "0" + binario 
    else:
        binario = "1" + binario 
    cociente = cociente // 2
print(cociente)
print(binario)

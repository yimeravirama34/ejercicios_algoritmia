# Algoritmo que pide al usuario tres fracciones para ser sumadas y dar su resultado en fraccionarios,
#primero se pide el numerador y luego el denominador de cada fraccion para asi, poder sacar el mcm 
# y lograr obtener la suma de las tres fracciones.

nume = int(input("primer numerador: "))
deno = int(input("primer denominador: "))
while deno == 0:
    print("** no es posible hacer divisiones entre cero***")
    deno = int(input("ingrese el primer denominador correcto: "))
nume2 = int(input("segundo numerador: "))
deno2 = int(input("segundo denominador: "))
while deno2 == 0:
    print("** no es posible hacer divisiones entre cero***")
    deno2 = int(input("ingrese el segundo denominador correcto: "))
nume3 = int(input("tercer numerador: "))
deno3 = int(input("tercer denominador: "))
while deno3 == 0:
    print("** no es posible hacer divisiones entre cero***")
    deno2 = int(input("ingrese el tercer denominador correcto: "))

def es_primo(x):
    cont = 0
    cont1 = 0
    medio = x//2
    for i in range(2, medio):
        if x % i == 0:
            cont += 1
            i = medio
        else:
            cont1 += 1
    if cont == 0:
        return cont
    else:
        return cont1
      
primo = 2
den = deno
den2 = deno2
den3 = deno3
mis_primos = []

while den > 1 and den2 > 1 and den3 > 1:
    contador = es_primo(primo)
    if contador == 0:
        if den % primo == 0 and den2 % primo == 0 and den3 % primo == 0:
            print(den, " ",den2, " ", den3, "  |  ", primo)
            den3 = den3 // primo
            den2 = den2 // primo
            den = den // primo
            mis_primos.append(primo)
        elif den % primo == 0 and den2 % primo == 0 and den3 % primo != 0:
            print(den, " ",den2, " ", den3, "  |  ", primo)
            den2 = den2 // primo
            den = den // primo
            mis_primos.append(primo)
        elif den % primo == 0 and den2 % primo != 0 and den3 % primo == 0:
            print(den, " ",den2, " ", den3, "  |  ", primo)
            den3 = den3 // primo
            den = den // primo
            mis_primos.append(primo)
        elif den % primo == 0 and den2 % primo != 0 and den3 % primo != 0:
            print(den, " ",den2, " ", den3, "  |  ", primo)
            den = den // primo
            mis_primos.append(primo)

        elif den % primo != 0 and den2 % primo == 0 and den3 % primo == 0:
            print(den, " ",den2, " ", den3, "  |  ", primo)
            den3 = den3 // primo
            den2 = den2 // primo
            mis_primos.append(primo)
        elif den % primo != 0 and den2 % primo == 0 and den3 % primo != 0:
            print(den, " ",den2, " ", den3, "  |  ", primo)
            den2 = den2 // primo
            mis_primos.append(primo)
        elif den % primo != 0 and den2 % primo != 0 and den3 % primo == 0:
            print(den, " ",den2, " ", den3, "  |  ", primo)
            den3 = den3 // primo
            mis_primos.append(primo)
            
        else:
            primo += 1
    else:
        primo += 1

print("los datos de la lista son: ", mis_primos)
print(len(mis_primos))
tamaño = len(mis_primos)
mcm = 1
i = 0
for i in range(tamaño):
    mcm = mcm*mis_primos[i]
print(mcm)
num1 = mcm / deno
num2 = mcm / deno2
num3 = mcm / deno3
resul = (nume * num1) + (nume2 * num2) + (nume3 * num3)
print("La suma de los tres fraccionarios es: ", resul, " / ", mcm)

    
              
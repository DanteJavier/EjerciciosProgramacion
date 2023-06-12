numeros = []
print("Para comenzar ingresaremos 10 números negativos: ")
for i in range(15):
    numero = int(input("Ingrese un número negativo: "))
    numeros.append(numero)
for i in range (len(numeros)):
    numeros[i] = (numeros[i]*(-1))

print("Los números positivos son:")
print(*numeros,sep=", ")
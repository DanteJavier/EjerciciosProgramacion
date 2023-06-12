numeros = []
suma = 0
print("Para comenzar ingresaremos 10 números: ")
for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
positivos = []
for i in numeros:
    if i > 0:
        suma = suma + i
        positivos.append(i)

print("Los números positivos son:")
print(*positivos,sep=", ")
print(f"Y su sumatoria es {suma}")

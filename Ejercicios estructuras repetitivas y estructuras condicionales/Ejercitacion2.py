numeros = []
menor = 0
print("Ingrese 10 números para comenzar a operar.")
for i in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

for i in numeros:
    if i < 100:
        menor += 1

numeros.sort()
print(f"La cantidad de numeros menores a 100 son {menor}")
print(f"El menor número es {numeros[0]} y el mayor es {numeros[-1]}")
numero = 0
a = 0
suma = 0
while a < 4:
    numero = int(input("Ingrese un numero: "))
    
    if numero % 2 == 0:
        suma = suma + numero
    a += 1
    
print(f"La suma de los números pares es: {suma}.")


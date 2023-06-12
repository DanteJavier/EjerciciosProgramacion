numero = 0
a = 0
suma = 0
par = 0
while a < 4:
    numero = int(input("Ingrese un numero: "))
    
    if numero % 2 == 0:
        suma = suma + numero
        par += 1
    a += 1
    
print(f"Los numeros pares son {par} y su suma es: {suma}.")


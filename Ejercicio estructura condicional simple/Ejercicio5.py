def dolaresPesos(dolares,valorDolar):
    return (dolares * valorDolar)

valorDolar = float(input("Ingrese el valor de dolar hoy en pesos: $"))
dolares = float(input("Ingrese la cantidad de dolares: U$S"))

print(f"El cambio total seria de ${dolaresPesos(dolares,valorDolar)}")
dolares = 0
pesos = 0
valorDolar = 0 
tipoDeCalculo = ""
continuar = "s"

def dolaresPesos(dolares,valorDolar):
    return (dolares * valorDolar)

def pesosDolares(pesos,valorDolar):
    return(pesos/valorDolar)


print("Bienvenido a la calculadora cambiaria")
while continuar.lower() == "s":
    tipoDeCalculo = input("Si desea cambiar de pesos a dolares ingrese 1.\nSi desea cambiar de dolares a pesos ingrese 2.\n")
    if tipoDeCalculo == "1":
        valorDolar = float(input("Ingrese el valor de dolar hoy en pesos: $"))
        pesos = float(input("Ingrese la cantidad de pesos a cambiar: $"))
        print(f"El cambio total seria de ${pesosDolares(pesos,valorDolar)}")

    elif tipoDeCalculo == "2":
        valorDolar = float(input("Ingrese el valor de dolar hoy en pesos: $"))
        dolares = float(input("Ingrese la cantidad de dolares a cambiar: $"))
        print(f"El cambio total seria de ${dolaresPesos(dolares,valorDolar)}")

    else:
        print("Ingreso una opcion incorrecta.")
    continuar = input("Si desea continuar calculando ingrese S: ")
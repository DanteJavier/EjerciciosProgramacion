primeraLetra = input("Ingrese la primer letra a comparar: ")
segundaLetra = input("Ingrese la segunda letra a comparar: ")

if primeraLetra.lower() == segundaLetra.lower():
    print(f"Las letras {primeraLetra.upper()} y {segundaLetra.upper()} son iguales")
else:
    print(f"Las letras {primeraLetra.upper()} y {segundaLetra.upper()} no son iguales")
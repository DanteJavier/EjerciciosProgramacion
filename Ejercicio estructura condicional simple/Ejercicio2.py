primeraPalabra = input("Ingrese la primer palabra a comparar: ")
segundaPalabra = input("Ingrese la segunda palabra a comparar: ")

if primeraPalabra.lower() == segundaPalabra.lower():
    print(f"Las palabras {primeraPalabra.upper()} y {segundaPalabra.upper()} son iguales")
else:
    print(f"Las palabras {primeraPalabra.upper()} y {segundaPalabra.upper()} no son iguales")
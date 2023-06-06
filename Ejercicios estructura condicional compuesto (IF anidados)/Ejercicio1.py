x = 0
print("Bienvenido al identificador de triángulos.")
while x != 5:
    try:
        lado1= float(input("Ingrese el lado 1 del triángulo: "))
        lado2= float(input("Ingrese el lado 2 del triángulo: "))
        lado3= float(input("Ingrese el lado 3 del triángulo: "))
        break
    except:
        x += 1
        print("Un valor ingresado no corresponde. Vuelva a intentar.")
if x != 5:
    if lado1 == lado2 and lado2 == lado3:
        print("El triángulo ingresado es equilatero.")
    elif lado1 == lado2 and lado2 != lado3:
        print("El triángulo ingresado es isósceles.")
    else:
        print("El triángulo ingresado es escaleno.")
else:
    print("Sobre paso la cantidad e errores, programa finalizado.")
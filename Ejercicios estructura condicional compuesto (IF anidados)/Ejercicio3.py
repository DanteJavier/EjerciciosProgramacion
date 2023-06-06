numeros = []
j=0
x = 0
while x != 3:
    try:
        while j < 3:
            numero = int(input("Ingrese un numero: "))
            numeros.append(numero)
            j += 1
        break
    except:
        x += 1
        print("Un valor ingresado no corresponde. Vuelva a intentar.")

if x !=3 and j==3:
    numeros.sort(reverse=True)
    if numeros[0]%2 == 0:
        print(f"El numero mayor es {numeros[0]} y es Par.")
    else:
        print(f"El numero mayor es {numeros[0]} y es Impar.")
else:
    print("Sobre paso la cantidad e errores, programa finalizado.")

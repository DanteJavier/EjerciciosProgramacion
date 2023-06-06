meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
x = 0
while x != 3:
    try:
        mes= int(input("Ingrese un numero entre 1 y 12: "))
        if mes > 0 and mes <= 12:
            break
        else:
            x += 1
            print("El valor ingresado no se encuentra entre 1 y 12.")
    except:
        x += 1
        print("Un valor ingresado no corresponde. Vuelva a intentar.")

if x != 3:
    print(f"El valor ingresado corresponde al mes de {meses[mes-1]}")
else:
    print("Sobre paso la cantidad e errores, programa finalizado.")
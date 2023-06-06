dias = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
x = 0
while x != 3:
    try:
        dia= int(input("Ingrese un numero entre 1 y 7: "))
        if dia > 0 and dia <= 7:
            break
        else:
            x += 1
            print("El valor ingresado no se encuentra entre 1 y 7.")
    except:
        x += 1
        print("Un valor ingresado no corresponde. Vuelva a intentar.")

if x != 3:
    print(f"El valor ingresado corresponde al día {dias[dia-1]}")
else:
    print("Sobre paso la cantidad e errores, programa finalizado.")
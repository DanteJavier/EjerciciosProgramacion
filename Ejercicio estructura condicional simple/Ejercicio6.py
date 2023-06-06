while True:
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            break
        except:
            print("El valor ingresado no corresponde. Vuelva a intentar.")

    if edad <= 15:
        print("Usted no se encuentra habilitado para votar por ser menor de edad.")
    elif edad >= 16:
        print("Usted se encuentra habilitado para votar.")

    continuar = input("Si desea continuar ingrese S: ")
    if continuar.lower() != "s":
        print("Muchas gracias.")
        break
    
x = "s"

while x.lower() == "s":
    sexo = input("Ingrese 'F' o 'M' para determinar la mesa a votar: ")
    if sexo.upper() == "F":
        print("Usted debe votar en la mesa femenina.")
    elif sexo.upper() == "M":
        print("Usted debe votar en la mesa masculina.")
    else:
        print("Usted ingreso un dato erroneo.")
    x = input("Si desea continuar ingrese 'S': ")

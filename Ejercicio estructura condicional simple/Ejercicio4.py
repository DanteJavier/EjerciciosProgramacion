a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a<b:
    print(f"{a} es menor que {b}")
elif a>b:
    print(f"{a} es mayor que {b}")
elif a==b:
    print(f"{a} es igual que {b}")
else:
    print("El dato ingresado no es correcto.")
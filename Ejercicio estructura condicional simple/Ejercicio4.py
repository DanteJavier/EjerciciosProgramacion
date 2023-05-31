a = ""
b = ""
while a == "":
    try:
        a = int(input("Ingrese el primer número: "))
    except:
        print("El valor ingresado no es un numero.")

while b == "":
    try:
        b = int(input("Ingrese el segundo número: "))
    except:
        print("El valor ingresado no es un numero.")
        
if a<b:
    print(f"{a} es menor que {b}")
elif a>b:
    print(f"{a} es mayor que {b}")
elif a==b:
    print(f"{a} es igual que {b}")
else:
    print("El dato ingresado no es correcto.")
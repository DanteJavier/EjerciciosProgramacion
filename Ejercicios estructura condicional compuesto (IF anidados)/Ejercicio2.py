importe = 0.0
tipoDePago = 0
while True:
    try:
        importe = float(input("Ingrese el precio del producto: "))
        tipoDePago = int(input("¿Que tipo de metodo de pago desea utilizar?\nIngrese (1) para contado. \nIngrese (2) para tarjeta. \nIngrese (3) para débito.\n"))
        
        if tipoDePago == 1:
            print(f"El precio del producto de es de ${importe}")
            print(f"El descuento por pago contado es de ${round(importe*0.1,2)}")
            print(f"El precio final es de ${round(importe - (importe*0.1),2)}")
            break
        elif tipoDePago == 2:
            print(f"El precio del producto de es de ${importe}")
            print(f"El interes por pago con tarjeta es de ${round(importe*0.1,2)}")
            print(f"El precio final es de ${round(importe + (importe*0.1),2)}")
            break
        elif tipoDePago == 3:
            print(f"El precio del producto de es de ${importe}")
            print(f"El descuento por pago con débito es de ${round(importe*0.15,2)}")
            print(f"El precio final es de ${round(importe - (importe*0.15),2)}")
            break
        else:
            print("El eligio una opcion incorrecta, vuelva a intentar.")
    except:
        print("Vuelva a intentar")        

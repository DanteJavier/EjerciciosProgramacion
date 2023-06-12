persona = []
personas = []
mayores = 0
menores = 0
hombres = 0
mujeres = 0
print("Para comenzar se leeran los datos de 15 personas: ")
for i in range(4):
    edad = int(input("Ingrese la edad: "))
    sexo = input("Ingrese el sexo (F) o (M): ").lower()
    persona.append(edad)
    persona.append(sexo)
    personas.append(persona)
    persona = []
for i in personas:
    if i[0] >= 18:
        mayores += 1
    else:
        menores += 1

    if i[1] == "m":
        hombres += 1
    else:
        mujeres +=1

print(f"Hay un total de {mujeres} mujeres y {hombres} hombres.")
print(f"De los cuales {mayores} son mayores y {menores} son menores.")


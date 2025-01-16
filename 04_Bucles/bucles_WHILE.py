i = 1

while i <= 10:
    print(i)
    i = i + 1

edad = int(input("Introduce tu edad "))
intentos = 0
while edad <= 0:
    print("Has introdudido una edad no validad")

    if intentos == 5:
        print("Superaste el numero de intentos")
        break

    edad = int(input("Introduce tu edad otra vez "))

    if edad <= 0:
        intentos = intentos + 1

if intentos < 5:
    print("Edad correcta")
else:
    print("Hasta luego")

#CONTINUE VUELVE A LA PRIMERA LINEA DEL BUCLE IGNORANDO LO QUE SEGUIA 
for letra in "phyton":
    if letra == "h":
        continue
    print(letra)

nombre = "Hello world"
print(len(nombre))

contador = 0
for i in nombre:
    if i == " ":
        continue
    contador = contador + 1

print(contador)


#PASS DEVUELVE UN NULL Y HACE COMO SI EL BUCLE NUNCA SE HAYA EJECUTADO


#ELSE

mail = input("introduce el mail: ")

for letra in mail:
    if letra == "@":
        arroba = True
        break

else:
    arroba = False

print(arroba)
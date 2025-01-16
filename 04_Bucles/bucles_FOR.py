numeros = [1,3,3]

#SE RECORRERA 3 VECES YA QUE LA LISTA TIENE 3 DE LONGITUD
for i in numeros: 
    print("Hola", i)
    #PODEMOS IMPRIMIRLO TODO JUTNO con end
    #print("Hola", end=" ja ")

#SI PONEMOS QUE RECORRA UN STRING, RECORRERA TANTAS VECES COMO LETRAS LA PALABRA O FRASE
palabra = "Hello world"
for i in palabra:
    print("hola", i)

email = False
mail = "example@gmail.com"

for i in mail:
    if i == "@":
        email = True

if email == True:
    print("Mail correcto")
else: 
    print("Mail incorrecto")

#SE PUEDE PONER EN UN RANGO DETERMINADO (6, 10) O QUE VAYA EN ESE RANGO HACIENDO SALTOS (6, 10, 2)
for i in range(6):
    print(f"valor {i}")